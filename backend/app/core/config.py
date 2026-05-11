from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "Basketball Platform API"
    app_env: str = "local"
    api_v1_prefix: str = "/api/v1"
    cors_origins: str = "http://localhost:5173"
    database_url: str = Field(
        default="postgresql+psycopg://basketball:basketball_dev_password@localhost:5432/basketball_platform"
    )
    mongodb_uri: str = "mongodb://localhost:27017/basketball_platform"
    log_level: str = "INFO"


@lru_cache
def get_settings() -> Settings:
    return Settings()
