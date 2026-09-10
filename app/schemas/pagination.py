"""Pagination request parameters and response envelope
(docs/conventions.md, section 9).
"""

from pydantic import BaseModel, Field

from app.core.constants import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE

__author__ = "Lucas Barros"
__version__ = "0.1.0"
__maintainer__ = "Lucas Barros"
__email__ = "lucasbarros2000@hotmail.com"
__status__ = "Development"


class PaginationParams(BaseModel):
    """Query parameters accepted by every paginated listing endpoint."""

    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE)

    @property
    def skip(self) -> int:
        """Number of documents to skip for this page (0-indexed)."""
        return (self.page - 1) * self.page_size


class PaginatedResponse[ItemT](BaseModel):
    """Standard envelope for paginated collection responses."""

    items: list[ItemT]
    page: int
    page_size: int
    total: int
    pages: int

    @classmethod
    def build(cls, items: list[ItemT], params: PaginationParams, total: int) -> "PaginatedResponse[ItemT]":
        """Build the envelope from the raw items, the request params and the total count."""
        pages = -(-total // params.page_size)  # ceil division; total=0 -> pages=0
        return cls(items=items, page=params.page, page_size=params.page_size, total=total, pages=pages)
