"""Authentication endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import get_current_user
from app.core.security import create_access_token, verify_password
from app.models.user import User
from app.schemas.auth import LoginRequest, TokenResponse
from app.schemas.user import UserRead

__author__ = "Lucas Barros"
__version__ = "0.1.0"
__maintainer__ = "Lucas Barros"
__email__ = "lucasbarros2000@hotmail.com"
__status__ = "Development"


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse)
async def login(payload: LoginRequest) -> TokenResponse:
    """Authenticate an internal staff user and return a JWT."""
    user = await User.find_one(User.email == payload.email)
    if user is None or not user.active or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="E-mail ou senha inválidos.")

    token = create_access_token(user.id, user.role)
    return TokenResponse(access_token=token, user=UserRead.model_validate(user, from_attributes=True))


@router.get("/me", response_model=UserRead)
async def me(user: User = Depends(get_current_user)) -> UserRead:
    """Return the currently authenticated user."""
    return UserRead.model_validate(user, from_attributes=True)
