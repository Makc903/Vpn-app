from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, Header, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .db import Base, engine, get_db
from .models import AccessKey, Payment, Server, ServerStatus, User
from .schemas import AuthRequest, AuthResponse, ConfigResponse, ReportRequest, TelegramPaymentWebhook
from .security import generate_token, hash_token, verify_token
from .settings import settings

app = FastAPI(title=settings.app_name)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def find_key(db: AsyncSession, token: str) -> AccessKey:
    # MVP lookup: scan hashes. For production store HMAC(token) indexed + bcrypt separately.
    rows = (await db.execute(select(AccessKey).where(AccessKey.is_active == True))).scalars().all()
    for key in rows:
        if verify_token(token, key.token_hash):
            return key
    raise HTTPException(status_code=401, detail="Invalid key")

def ensure_active(key: AccessKey):
    if not key.is_active or key.expires_at <= datetime.utcnow():
        raise HTTPException(status_code=403, detail="Subscription expired")

@app.get("/health")
async def health():
    return {"ok": True, "time": datetime.utcnow().isoformat()}

@app.post("/api/client/auth", response_model=AuthResponse)
async def auth(payload: AuthRequest, db: AsyncSession = Depends(get_db)):
    key = await find_key(db, payload.token)
    return AuthResponse(
        user_id=key.user_id,
        expire_date=key.expires_at,
        subscription_active=key.expires_at > datetime.utcnow() and key.is_active,
    )

@app.get("/api/client/config", response_model=ConfigResponse)
async def config(token: str, db: AsyncSession = Depends(get_db)):
    key = await find_key(db, token)
    ensure_active(key)
    servers = (await db.execute(
        select(Server).where(Server.status == ServerStatus.active).order_by(Server.load_score.asc())
    )).scalars().all()
    if not servers:
        raise HTTPException(status_code=503, detail="No active VPN servers")
    primary = servers[0]
    rendered = primary.config_template.replace("{{USER_ID}}", str(key.user_id)).replace("{{TOKEN}}", token)
    return ConfigResponse(
        server_id=primary.id,
        country=primary.country,
        city=primary.city,
        protocol=primary.protocol,
        endpoint=primary.endpoint,
        public_key=primary.public_key,
        config=rendered,
        failover_server_ids=[s.id for s in servers[1:4]],
    )

@app.post("/api/client/report")
async def report(payload: ReportRequest, db: AsyncSession = Depends(get_db)):
    key = await find_key(db, payload.token)
    key.used_bytes += max(payload.tx_bytes, 0) + max(payload.rx_bytes, 0)
    await db.commit()
    return {"ok": True, "used_bytes": key.used_bytes}

@app.post("/api/telegram/payment-success")
async def payment_success(payload: TelegramPaymentWebhook, x_api_secret: str = Header(default=""), db: AsyncSession = Depends(get_db)):
    if x_api_secret != settings.api_secret:
        raise HTTPException(status_code=401, detail="Bad API secret")
    user = (await db.execute(select(User).where(User.tg_user_id == payload.tg_user_id))).scalar_one_or_none()
    if user is None:
        user = User(tg_user_id=payload.tg_user_id)
        db.add(user)
        await db.flush()
    payment = Payment(user_id=user.id, provider="telegram", provider_payment_id=payload.provider_payment_id, amount=payload.amount, currency=payload.currency, status="paid")
    db.add(payment)
    key = (await db.execute(select(AccessKey).where(AccessKey.user_id == user.id, AccessKey.is_active == True))).scalars().first()
    if key is None:
        raw_token = generate_token()
        key = AccessKey(user_id=user.id, token_hash=hash_token(raw_token), expires_at=datetime.utcnow() + timedelta(days=payload.days))
        db.add(key)
        await db.commit()
        return {"ok": True, "token": raw_token, "expires_at": key.expires_at}
    key.expires_at = max(key.expires_at, datetime.utcnow()) + timedelta(days=payload.days)
    await db.commit()
    return {"ok": True, "expires_at": key.expires_at}

@app.post("/admin/seed", include_in_schema=False)
async def seed(x_api_secret: str = Header(default=""), db: AsyncSession = Depends(get_db)):
    if x_api_secret != settings.api_secret:
        raise HTTPException(status_code=401, detail="Bad API secret")
    server = Server(
        country="NL",
        city="Amsterdam",
        protocol="vless",
        endpoint="vpn1.example.com:443",
        public_key="replace-with-server-public-key",
        config_template='{"type":"vless","server":"vpn1.example.com","server_port":443,"uuid":"{{TOKEN}}","tls":{"enabled":true,"server_name":"cdn.example.com"}}',
    )
    db.add(server)
    await db.commit()
    return {"ok": True}
