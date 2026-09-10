"""One-off script: create the initial Administrator user.

Reads credentials from the environment (SEED_ADMIN_EMAIL,
SEED_ADMIN_PASSWORD) — never hardcoded.

Usage (run from the project root, so `app` is importable):
    uv run python -m scripts.seed_admin
"""

import asyncio

from app.core.config import get_settings
from app.core.security import hash_password
from app.db.client import close_database_connection, init_database
from app.models.user import User, UserRole

__author__ = "Lucas Barros"
__version__ = "0.1.0"
__maintainer__ = "Lucas Barros"
__email__ = "lucasbarros2000@hotmail.com"
__status__ = "Development"


async def seed_admin() -> None:
    """Create the initial Administrator user if it does not already exist."""
    settings = get_settings()
    await init_database()

    existing = await User.find_one(User.email == settings.seed_admin_email)
    if existing is not None:
        print(f"Usuário administrador '{settings.seed_admin_email}' já existe — nada a fazer.")
        await close_database_connection()
        return

    admin = User(
        name="Administrador",
        email=settings.seed_admin_email,
        password_hash=hash_password(settings.seed_admin_password),
        role=UserRole.ADMIN,
    )
    await admin.insert()
    print(f"Usuário administrador '{settings.seed_admin_email}' criado com sucesso.")
    await close_database_connection()


if __name__ == "__main__":
    asyncio.run(seed_admin())
