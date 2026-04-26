from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "VPN MVP API"
    database_url: str = "postgresql+asyncpg://vpn:vpn@db:5432/vpn"
    api_secret: str = "change-me"
    telegram_bot_token: str = ""
    public_api_base: str = "https://api.example.com"

    class Config:
        env_file = ".env"

settings = Settings()
