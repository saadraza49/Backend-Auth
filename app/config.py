"""
Application Configuration
─────────────────────────
Uses pydantic-settings to load environment variables from .env file.

All secrets (SECRET_KEY, DATABASE_URL, etc.) live in .env and are
validated at startup — the app will refuse to start if any are missing.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central configuration loaded from environment variables / .env file.

    Attributes
    ----------
    DATABASE_URL : str
        PostgreSQL connection string.
        Format: postgresql+psycopg://user:pass@host:port/dbname
    SECRET_KEY : str
        Used to **sign** JWT tokens (HMAC key).
        • Changing this key invalidates every previously issued token.
        • Must be long, random, and kept secret.
        • Generate one with:  python -c "import secrets; print(secrets.token_hex(32))"
    ALGORITHM : str
        JWT signing algorithm.  HS256 = HMAC with SHA-256.
        This is a *string* identifier, not a number.
    ACCESS_TOKEN_EXPIRE_MINUTES : int
        Lifetime of an access token in minutes.
    """

    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Tell pydantic-settings to read from a .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


# Singleton — imported everywhere as `from app.config import settings`
settings = Settings()
