"""Internal staff user: authentication and role-based access control."""

from datetime import UTC, datetime
from enum import StrEnum
from typing import Annotated
from uuid import UUID, uuid4

from beanie import Document, Indexed
from pydantic import Field

__author__ = "Lucas Barros"
__version__ = "0.1.0"
__maintainer__ = "Lucas Barros"
__email__ = "lucasbarros2000@hotmail.com"
__status__ = "Development"


class UserRole(StrEnum):
    """Internal staff roles (docs/mvp.md, section 3.1).

    The seventh profile from the functional guide, "Cliente final", is not
    represented here: the end customer does not authenticate through this
    system (see docs/mvp.md, section 4.2) and belongs to a future `Customer`
    document, not to `User`.
    """

    ADMIN = "admin"
    MANAGER = "manager"
    KITCHEN = "kitchen"
    DISPATCH = "dispatch"
    SUPPORT = "support"
    INVENTORY = "inventory"


class User(Document):
    """An internal staff member able to authenticate and act on the API."""

    id: UUID = Field(default_factory=uuid4)
    name: str
    email: Annotated[str, Indexed(unique=True)]
    password_hash: str
    role: UserRole
    active: bool = True
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    class Settings:
        name = "users"
