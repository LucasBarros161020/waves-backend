"""Tracks connected WebSocket clients and broadcasts real-time events."""

from datetime import UTC, datetime
from typing import Any

from fastapi import WebSocket

__author__ = "Lucas Barros"
__version__ = "0.1.0"
__maintainer__ = "Lucas Barros"
__email__ = "lucasbarros2000@hotmail.com"
__status__ = "Development"


class ConnectionManager:
    """Holds active WebSocket connections and broadcasts events to all of them."""

    def __init__(self) -> None:
        self._connections: set[WebSocket] = set()

    async def connect(self, websocket: WebSocket) -> None:
        """Accept a WebSocket connection and start tracking it."""
        await websocket.accept()
        self._connections.add(websocket)

    def disconnect(self, websocket: WebSocket) -> None:
        """Stop tracking a WebSocket connection."""
        self._connections.discard(websocket)

    async def broadcast(self, event: str, data: dict[str, Any]) -> None:
        """Send an `{event, data, occurred_at}` message to every connected client.

        A connection that fails to receive the message (e.g. it dropped
        without a clean close) is disconnected instead of raising, so one
        broken client cannot interrupt delivery to the others.
        """
        message = {
            "event": event,
            "data": data,
            "occurred_at": datetime.now(UTC).isoformat(),
        }

        stale_connections: list[WebSocket] = []
        for connection in self._connections:
            try:
                await connection.send_json(message)
            except Exception:  # noqa: BLE001 - any failure means the connection is dead
                stale_connections.append(connection)

        for connection in stale_connections:
            self.disconnect(connection)


connection_manager = ConnectionManager()
