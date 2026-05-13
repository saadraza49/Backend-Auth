"""
Security Utilities — Password Hashing & JWT Tokens
───────────────────────────────────────────────────

Password Hashing
    Uses passlib's CryptContext with bcrypt.
    • hash_password()   → returns a one-way bcrypt hash
    • verify_password() → constant-time comparison

JWT Tokens
    Uses python-jose (JOSE = JSON Object Signing and Encryption).
    • create_access_token() → signs a payload with HS256

    HS256 explained:
        "HS256" stands for **HMAC with SHA-256**.
        • HMAC = Hash-based Message Authentication Code
        • SHA-256 = Secure Hash Algorithm producing a 256-bit digest
        • It is a *symmetric* algorithm: the same SECRET_KEY is used
          to both sign and verify the token.
        • The value is a **string** ("HS256"), not a number.
"""

from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

from app.config import settings


# ── Password Hashing ────────────────────────────────────────────────

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def hash_password(plain_password: str) -> str:
    """Return a bcrypt hash of the given plain-text password."""
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain-text password against its bcrypt hash.
    Uses constant-time comparison to prevent timing attacks.
    """
    return pwd_context.verify(plain_password, hashed_password)


# ── JWT Token Creation ──────────────────────────────────────────────

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Create a signed JWT access token.

    Parameters
    ----------
    data : dict
        Payload to encode (typically {"sub": email}).
    expires_delta : timedelta | None
        Custom expiration. Falls back to ACCESS_TOKEN_EXPIRE_MINUTES.

    Returns
    -------
    str
        Encoded JWT string.
    """
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + (
        expires_delta
        if expires_delta
        else timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,  # "HS256" — a string, not a number
    )
