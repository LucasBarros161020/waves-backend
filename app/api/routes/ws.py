"""Real-time WebSocket endpoint."""

from uuid import UUID

import jwt
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, status

from app.core.security import decode_access_token
from app.models.user import User
from app.ws.manager import connection_manager

__author__ = "Lucas Barros"
__version__ = "0.1.0"
__maintainer__ = "Lucas Barros"
__email__ = "lucasbarros2000@hotmail.com"
__status__ = "Development"


router = APIRouter(tags=["realtime"])


async def _authenticate(token: str | None) -> User | None:
    """Resolve the User a WebSocket connection's `token` query param belongs to."""
    if token is None:
        return None

    try:
        payload = decode_access_token(token)
        user_id = UUID(payload["sub"])
    except (jwt.InvalidTokenError, KeyError, ValueError):
        return None

    user = await User.get(user_id)
    if user is None or not user.active:
        return None
    return user


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: str | None = None) -> None:
    """Accept a WebSocket connection authenticated via a `token` query param.

    Real-time events use a query-string token (rather than the
    `Authorization` header used by HTTP endpoints) because browser
    WebSocket clients cannot set custom request headers.
    """
    user = await _authenticate(token)
    if user is None:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    await connection_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        connection_manager.disconnect(websocket)
