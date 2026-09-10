"""Request/response schemas for the User resource."""

from datetime import datetime
from typing import Self
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field, model_validator

from app.models.user import UserRole

__author__ = "Lucas Barros"
__version__ = "0.1.0"
__maintainer__ = "Lucas Barros"
__email__ = "lucasbarros2000@hotmail.com"
__status__ = "Development"


_MIN_PASSWORD_LENGTH = 8


class UserCreate(BaseModel):
    """Payload to create a new internal staff user (admin-only)."""

    name: str
    email: EmailStr
    role: UserRole
    password: str = Field(min_length=_MIN_PASSWORD_LENGTH)
    confirm_password: str

    @model_validator(mode="after")
    def passwords_must_match(self) -> Self:
        if self.password != self.confirm_password:
            raise ValueError("As senhas informadas não coincidem.")
        return self


class UserRead(BaseModel):
    """Public representation of a User, returned by the API."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    email: EmailStr
    role: UserRole
    active: bool
    created_at: datetime
