

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserCreate, UserResponse, Token
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    description="Creates a new user account. Returns the user profile (without password).",
)
def register(
    payload: UserCreate,
    db: Session = Depends(get_db),
):
    return AuthService.register_user(payload, db)


@router.post(
    "/login",
    response_model=Token,
    summary="Login",
    description=(
        "Authenticate and receive a JWT access token. "
        "Enter your **email** in the username field."
    ),
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    return AuthService.authenticate_user(
        email=form_data.username,  # Swagger sends email in the "username" field
        password=form_data.password,
        db=db,
    )
