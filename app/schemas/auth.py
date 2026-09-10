"""Request/response schemas for authentication."""

from pydantic import BaseModel, EmailStr

from app.schemas.user import UserRead

__author__ = "Lucas Barros"
__version__ = "0.1.0"
__maintainer__ = "Lucas Barros"
__email__ = "lucasbarros2000@hotmail.com"
__status__ = "Development"


class LoginRequest(BaseModel):
    """Credentials submitted to POST /auth/login."""

    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    """Response returned by a successful login."""

    access_token: str
    token_type: str = "bearer"
    user: UserRead
