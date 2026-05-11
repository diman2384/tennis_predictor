from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings."""
    
    # App
    APP_NAME: str = "Tennis Predictor"
    DEBUG: bool = False
    
    # Database
    DATABASE_URL: str = ""
    DATABASE_URL_SYNC: str = ""
    
    # Redis
    REDIS_URL: str = ""
    
    # Telegram
    TELEGRAM_BOT_TOKEN: str = ""
    TELEGRAM_BOT_USERNAME: str = ""
    
    # Mini App
    MINI_APP_URL: str = "http://localhost:5173"
    
    # Tennis API
    TENNIS_API_URL: str = "https://api.example.com"
    TENNIS_API_KEY: str = ""
    
    # News API
    NEWS_API_KEY: str = ""
    
    # LLM
    LLM_API_KEY: str = ""
    LLM_MODEL: str = "gpt-3.5-turbo"
    
    # Security
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings."""
    return Settings()
