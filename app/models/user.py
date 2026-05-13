
from datetime import datetime, timezone

from sqlalchemy import String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    """
    SQLAlchemy 2.0-style User model.

    Columns
    -------
    id              : int   — auto-increment primary key
    username        : str   — unique, indexed
    email           : str   — unique, indexed
    hashed_password : str   — bcrypt hash (never store plain text!)
    is_active       : bool  — soft-delete / deactivation flag
    created_at      : datetime — server-default UTC timestamp
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True, index=True, autoincrement=True
    )
    username: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(255), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(255), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, server_default="true"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
    )

    def __repr__(self) -> str:
        return f"<User id={self.id} username={self.username!r}>"
