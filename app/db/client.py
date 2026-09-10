"""MongoDB client and Beanie initialization."""

from beanie import init_beanie
from pymongo import AsyncMongoClient

from app.core.config import get_settings

__author__ = "Lucas Barros"
__version__ = "0.1.0"
__maintainer__ = "Lucas Barros"
__email__ = "lucasbarros2000@hotmail.com"
__status__ = "Development"


settings = get_settings()

# Beanie 2.x uses PyMongo's native async client (pymongo.AsyncMongoClient)
# directly; it no longer depends on Motor.
#
# uuidRepresentation="standard" avoids the legacy, driver-specific UUID byte
# orderings (pythonLegacy/javaLegacy/csharpLegacy) documented in
# docs/conventions.md (section 5.2).
client: AsyncMongoClient = AsyncMongoClient(
    settings.mongodb_url,
    uuidRepresentation="standard",
)

# Document models are registered here as they are implemented (see
# docs/conventions.md, section 4.24, for the project's schema evolution
# approach without a migrations framework).
document_models: list = []


async def init_database() -> None:
    """Initialize Beanie against the configured MongoDB database."""
    database = client[settings.mongodb_db_name]
    await init_beanie(database=database, document_models=document_models)


async def close_database_connection() -> None:
    """Close the underlying MongoDB client connection."""
    await client.close()
