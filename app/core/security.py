"""Password hashing and JWT helpers."""

from datetime import UTC, datetime, timedelta
from typing import Any
from uuid import UUID

import jwt
from pwdlib import PasswordHash

from app.core.config import get_settings
from app.models.user import UserRole

__author__ = "Lucas Barros"
__version__ = "0.1.0"
__maintainer__ = "Lucas Barros"
__email__ = "lucasbarros2000@hotmail.com"
__status__ = "Development"


settings = get_settings()
_password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    """Hash a plain-text password for storage."""
    return _password_hash.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    """Check a plain-text password against a stored hash."""
    return _password_hash.verify(password, password_hash)


def create_access_token(user_id: UUID, role: UserRole) -> str:
    """Create a signed JWT for an authenticated user."""
    expires_at = datetime.now(UTC) + timedelta(minutes=settings.access_token_expire_minutes)
    payload = {"sub": str(user_id), "role": role.value, "exp": expires_at}
    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def decode_access_token(token: str) -> dict[str, Any]:
    """Decode and validate a JWT.

    Raises `jwt.InvalidTokenError` (or a subclass) when the token is
    malformed, expired, or signed with a different key.
    """
    return jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
