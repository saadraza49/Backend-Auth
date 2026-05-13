"""
Database Engine & Session Management
─────────────────────────────────────
Creates the SQLAlchemy async-compatible engine, session factory,
declarative Base, and a FastAPI dependency for per-request sessions.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.config import settings


# ── Engine ──────────────────────────────────────────────────────────
# Using psycopg (v3) as the PostgreSQL driver.
# pool_pre_ping=True ensures stale connections are recycled.
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    echo=False,  # Set True for SQL logging during development
)

# ── Session Factory ─────────────────────────────────────────────────
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


# ── Declarative Base ────────────────────────────────────────────────
class Base(DeclarativeBase):
    """
    All ORM models inherit from this base.
    Alembic reads Base.metadata to autogenerate migrations.
    """
    pass


# ── Dependency ──────────────────────────────────────────────────────
def get_db():
    """
    FastAPI dependency that yields a database session per request
    and ensures it is closed afterwards.

    Usage in a route:
        @router.get("/items")
        def list_items(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
