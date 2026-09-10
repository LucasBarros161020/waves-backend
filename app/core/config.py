"""Application settings loaded from environment variables."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

__author__ = "Lucas Barros"
__version__ = "0.1.0"
__maintainer__ = "Lucas Barros"
__email__ = "lucasbarros2000@hotmail.com"
__status__ = "Development"


class Settings(BaseSettings):
    """Application configuration."""

    app_name: str = "Waves Backend"
    app_version: str = "0.1.0"
    environment: str = "development"
    debug: bool = True

    mongodb_url: str = "mongodb://waves:waves@localhost:27018/?authSource=admin"
    mongodb_db_name: str = "waves"

    jwt_secret_key: str = "change-me-to-a-random-secret-of-at-least-32-characters"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 480

    seed_admin_email: str = "admin@waves.com.br"
    seed_admin_password: str = "change-me-before-seeding"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return the cached application settings."""
    return Settings()