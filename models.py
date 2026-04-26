import enum
from datetime import datetime
from sqlalchemy import Boolean, DateTime, Enum, ForeignKey, Integer, String, BigInteger, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .db import Base

class ServerStatus(str, enum.Enum):
    active = "active"
    disabled = "disabled"
    blocked = "blocked"

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tg_user_id: Mapped[int | None] = mapped_column(BigInteger, unique=True, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    keys: Mapped[list["AccessKey"]] = relationship(back_populates="user")

class AccessKey(Base):
    __tablename__ = "keys"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    token_hash: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    expires_at: Mapped[datetime] = mapped_column(DateTime, index=True)
    max_devices: Mapped[int] = mapped_column(Integer, default=1)
    used_bytes: Mapped[int] = mapped_column(BigInteger, default=0)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    user: Mapped[User] = relationship(back_populates="keys")

class Server(Base):
    __tablename__ = "servers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    country: Mapped[str] = mapped_column(String(64))
    city: Mapped[str] = mapped_column(String(64), default="")
    protocol: Mapped[str] = mapped_column(String(32), default="vless")
    endpoint: Mapped[str] = mapped_column(String(255))
    public_key: Mapped[str | None] = mapped_column(Text, nullable=True)
    config_template: Mapped[str] = mapped_column(Text)
    load_score: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[ServerStatus] = mapped_column(Enum(ServerStatus), default=ServerStatus.active)

class Payment(Base):
    __tablename__ = "payments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    provider: Mapped[str] = mapped_column(String(64))
    provider_payment_id: Mapped[str] = mapped_column(String(128), unique=True)
    amount: Mapped[int] = mapped_column(Integer)
    currency: Mapped[str] = mapped_column(String(8), default="RUB")
    status: Mapped[str] = mapped_column(String(32), default="pending")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
