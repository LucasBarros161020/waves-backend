"""Structured (JSON) logging, one line per record, written to stdout.

Platforms such as Railway collect whatever a container writes to
stdout/stderr; emitting JSON lines lets that collector (or any downstream
log processor) parse fields directly instead of scraping free-form text.
"""

import json
import logging
import sys
from datetime import UTC, datetime
from typing import Any

__author__ = "Lucas Barros"
__version__ = "0.1.0"
__maintainer__ = "Lucas Barros"
__email__ = "lucasbarros2000@hotmail.com"
__status__ = "Development"


class JsonFormatter(logging.Formatter):
    """Render each log record as a single JSON line."""

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "timestamp": datetime.fromtimestamp(record.created, tz=UTC).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        return json.dumps(payload, ensure_ascii=False)


def configure_logging(level: int = logging.INFO) -> None:
    """Install a single JSON stdout handler on the root logger.

    Every logger that propagates to root — our own application loggers as
    well as uvicorn's — ends up emitting the same structured format. Uvicorn
    installs its own handlers by default; those are cleared first so records
    are not duplicated.
    """
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())

    root_logger = logging.getLogger()
    root_logger.handlers = [handler]
    root_logger.setLevel(level)

    for logger_name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
        uvicorn_logger = logging.getLogger(logger_name)
        uvicorn_logger.handlers = []
        uvicorn_logger.propagate = True
