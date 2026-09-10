"""Domain-level exceptions, mapped to the API's error envelope by the
global handlers in app/core/error_handlers.py.
"""

from typing import Any

__author__ = "Lucas Barros"
__version__ = "0.1.0"
__maintainer__ = "Lucas Barros"
__email__ = "lucasbarros2000@hotmail.com"
__status__ = "Development"


class DomainError(Exception):
    """Base class for errors raised deliberately by application/business logic."""

    status_code: int = 400

    def __init__(self, code: str, message: str, details: Any | None = None) -> None:
        self.code = code
        self.message = message
        self.details = details
        super().__init__(message)


class NotFoundError(DomainError):
    """Raised when a requested resource does not exist."""

    status_code = 404


class ConflictError(DomainError):
    """Raised when an operation conflicts with the current state of a resource."""

    status_code = 409


class BusinessRuleError(DomainError):
    """Raised when a business rule prevents an operation from completing."""

    status_code = 409
