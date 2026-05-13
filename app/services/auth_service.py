"""
Authentication Service Layer
─────────────────────────────
Business logic for registration and login.
Keeps route handlers thin and testable.
"""

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, Token
from app.core.security import hash_password, verify_password, create_access_token


class AuthService:
    """Encapsulates authentication business logic."""

    # ── Registration ────────────────────────────────────────────────

    @staticmethod
    def register_user(payload: UserCreate, db: Session) -> User:
        """
        Register a new user.

        Raises
        ------
        HTTPException 409
            If the username or email already exists.
        """

        # Check for duplicate email
        if db.query(User).filter(User.email == payload.email).first():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A user with this email already exists.",
            )

        # Check for duplicate username
        if db.query(User).filter(User.username == payload.username).first():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A user with this username already exists.",
            )

        new_user = User(
            username=payload.username,
            email=payload.email,
            hashed_password=hash_password(payload.password),
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    # ── Login ───────────────────────────────────────────────────────

    @staticmethod
    def authenticate_user(email: str, password: str, db: Session) -> Token:
        """
        Authenticate a user and return a JWT token.

        Raises
        ------
        HTTPException 401
            If the email doesn't exist or the password is wrong.
        """

        user = db.query(User).filter(User.email == email).first()

        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token = create_access_token(data={"sub": user.email})
        return Token(access_token=access_token)
