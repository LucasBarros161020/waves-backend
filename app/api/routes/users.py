"""User management endpoints (admin-only)."""

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import require_role
from app.core.security import hash_password
from app.models.user import User, UserRole
from app.schemas.pagination import PaginatedResponse, PaginationParams
from app.schemas.user import UserCreate, UserRead

__author__ = "Lucas Barros"
__version__ = "0.1.0"
__maintainer__ = "Lucas Barros"
__email__ = "lucasbarros2000@hotmail.com"
__status__ = "Development"


router = APIRouter(prefix="/users", tags=["users"])

_require_admin = Depends(require_role(UserRole.ADMIN))


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(
    payload: UserCreate,
    _: User = _require_admin,
) -> UserRead:
    """Create a new internal staff user. Restricted to Administrators."""
    existing = await User.find_one(User.email == payload.email)
    if existing is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Já existe um usuário com este e-mail.",
        )

    user = User(
        name=payload.name,
        email=payload.email,
        password_hash=hash_password(payload.password),
        role=payload.role,
    )
    await user.insert()
    return UserRead.model_validate(user, from_attributes=True)


@router.get("", response_model=PaginatedResponse[UserRead])
async def list_users(
    params: PaginationParams = Depends(),
    _: User = _require_admin,
) -> PaginatedResponse[UserRead]:
    """List internal staff users, paginated. Restricted to Administrators."""
    total = await User.find_all().count()
    users = await User.find_all().sort(-User.created_at).skip(params.skip).limit(params.page_size).to_list()
    items = [UserRead.model_validate(user, from_attributes=True) for user in users]
    return PaginatedResponse.build(items=items, params=params, total=total)
