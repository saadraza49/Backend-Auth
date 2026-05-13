"""
User Routes — /users
────────────────────
GET /users/me  → return the currently authenticated user
"""

from fastapi import APIRouter, Depends

from app.models.user import User
from app.schemas.user import UserResponse
from app.utils.deps import get_current_active_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "/me",
    response_model=UserResponse,
    summary="Get current user",
    description="Returns the profile of the currently authenticated user.",
)
def read_current_user(
    current_user: User = Depends(get_current_active_user),
):
    return current_user
