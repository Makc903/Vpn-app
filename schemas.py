from datetime import datetime
from pydantic import BaseModel

class AuthRequest(BaseModel):
    token: str
    device_id: str | None = None

class AuthResponse(BaseModel):
    user_id: int
    expire_date: datetime
    subscription_active: bool

class ConfigResponse(BaseModel):
    server_id: int
    country: str
    city: str
    protocol: str
    endpoint: str
    public_key: str | None = None
    config: str
    failover_server_ids: list[int]

class ReportRequest(BaseModel):
    token: str
    server_id: int
    tx_bytes: int = 0
    rx_bytes: int = 0

class TelegramPaymentWebhook(BaseModel):
    tg_user_id: int
    provider_payment_id: str
    amount: int
    currency: str = "RUB"
    days: int = 30
