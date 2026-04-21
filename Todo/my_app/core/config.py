# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    # DB
    database_url: str
    # JWT
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 10000
    #앱
    debug: bool = False
    app_name: str = "FastAPI App"
    model_config = SettingsConfigDict(
            env_file=".env",
            env_file_encoding="utf-8",
            case_sensitive=True,)
    
@lru_cache
def get_settings() -> Settings:
    return Settings()