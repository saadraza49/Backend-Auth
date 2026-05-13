

from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, ConfigDict


# ── Request Schemas ─────────────────────────────────────────────────

class UserCreate(BaseModel):
    """Schema for user registration."""

    username: str = Field(
        ..., min_length=3, max_length=50, examples=["johndoe"]
    )
    email: EmailStr = Field(
        ..., examples=["john@example.com"]
    )
    password: str = Field(
        ..., min_length=8, max_length=128, examples=["strongP@ssw0rd"]
    )


class UserLogin(BaseModel):
    """Schema for user login."""

    email: EmailStr = Field(
        ..., examples=["john@example.com"]
    )
    password: str = Field(
        ..., examples=["strongP@ssw0rd"]
    )


# ── Response Schemas ────────────────────────────────────────────────

class UserResponse(BaseModel):
    """
    Public-facing user representation.
    Never includes the hashed password.
    """

    id: int
    username: str
    email: EmailStr
    is_active: bool
    created_at: datetime

    # Pydantic v2: allow populating from ORM attributes
    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    """JWT token response returned after successful login."""

    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Payload extracted from a decoded JWT."""

    email: str | None = None
