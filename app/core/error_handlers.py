"""Global exception handlers.

Normalizes every error response to the {code, message, details} envelope
defined in docs/conventions.md (section 8), so the client never has to
interpret framework- or database-specific error shapes.
"""

import logging
from typing import Any

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.exceptions import DomainError

__author__ = "Lucas Barros"
__version__ = "0.1.0"
__maintainer__ = "Lucas Barros"
__email__ = "lucasbarros2000@hotmail.com"
__status__ = "Development"


logger = logging.getLogger("waves")

# Fallback `code` for HTTPException instances raised without going through a
# DomainError subclass (e.g. auth dependencies raising HTTPException(401)
# directly). Codes match the ones already fixed by docs/conventions.md 8.6.
_STATUS_CODE_FALLBACK = {
    status.HTTP_400_BAD_REQUEST: "INVALID_REQUEST",
    status.HTTP_401_UNAUTHORIZED: "UNAUTHORIZED",
    status.HTTP_403_FORBIDDEN: "FORBIDDEN",
    status.HTTP_404_NOT_FOUND: "NOT_FOUND",
    status.HTTP_409_CONFLICT: "CONFLICT",
    status.HTTP_422_UNPROCESSABLE_ENTITY: "VALIDATION_ERROR",
}
_DEFAULT_HTTP_ERROR_CODE = "HTTP_ERROR"

# Location segments FastAPI/Pydantic prepend to every validation error,
# stripped so `field` reads e.g. "quantity" instead of "body.quantity".
_VALIDATION_LOCATION_PREFIXES = {"body", "query", "path", "header"}


def _error_response(status_code: int, code: str, message: str, details: Any | None = None) -> JSONResponse:
    return JSONResponse(status_code=status_code, content={"code": code, "message": message, "details": details})


async def domain_error_handler(request: Request, exc: DomainError) -> JSONResponse:
    return _error_response(exc.status_code, exc.code, exc.message, exc.details)


async def http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    code = _STATUS_CODE_FALLBACK.get(exc.status_code, _DEFAULT_HTTP_ERROR_CODE)
    return _error_response(exc.status_code, code, str(exc.detail), None)


async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    details = [
        {
            "field": ".".join(
                str(part) for part in error["loc"] if part not in _VALIDATION_LOCATION_PREFIXES
            ),
            "message": error["msg"],
        }
        for error in exc.errors()
    ]
    return _error_response(
        status.HTTP_422_UNPROCESSABLE_ENTITY,
        "VALIDATION_ERROR",
        "Os dados enviados são inválidos.",
        details,
    )


async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.exception("Unhandled exception while processing %s %s", request.method, request.url.path)
    return _error_response(
        status.HTTP_500_INTERNAL_SERVER_ERROR,
        "INTERNAL_SERVER_ERROR",
        "Ocorreu um erro interno inesperado.",
        None,
    )


def register_error_handlers(app: FastAPI) -> None:
    """Register all global exception handlers on the FastAPI application."""
    app.add_exception_handler(DomainError, domain_error_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(Exception, unhandled_exception_handler)
