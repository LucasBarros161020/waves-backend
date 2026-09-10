"""Main entrypoint for the Waves Backend FastAPI application."""

import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import auth, users
from app.core.config import get_settings
from app.core.error_handlers import register_error_handlers
from app.core.logging import configure_logging
from app.db.client import close_database_connection, init_database

__author__ = "Lucas Barros"
__version__ = "0.1.0"
__maintainer__ = "Lucas Barros"
__email__ = "lucasbarros2000@hotmail.com"
__status__ = "Development"


settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Initialize and tear down application-wide resources."""
    configure_logging(logging.DEBUG if settings.debug else logging.INFO)
    await init_database()
    yield
    await close_database_connection()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
    lifespan=lifespan,
)

register_error_handlers(app)

app.include_router(auth.router)
app.include_router(users.router)


@app.get("/health", tags=["Health"])
async def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "environment": settings.environment,
    }