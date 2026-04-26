import secrets
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generate_token() -> str:
    return secrets.token_urlsafe(32)

def hash_token(token: str) -> str:
    return pwd_context.hash(token)

def verify_token(token: str, token_hash: str) -> bool:
    return pwd_context.verify(token, token_hash)
