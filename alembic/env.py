"""
Alembic Environment Configuration
──────────────────────────────────
What are migrations?
    Migrations are version-controlled changes to your database schema.
    Instead of manually running ALTER TABLE statements, Alembic generates
    Python scripts that describe each schema change, so your database
    evolves alongside your code.

Why Alembic?
    • Tracks every schema change as a versioned "revision" file.
    • Supports autogenerate — compares your SQLAlchemy models against the
      live database and generates the migration diff automatically.
    • Allows upgrading AND downgrading (rollback).
    • Works in teams — everyone applies the same ordered set of changes.

How schema changes are tracked:
    1. You modify a SQLAlchemy model (add column, change type, etc.).
    2. Run:  alembic revision --autogenerate -m "describe change"
       Alembic compares models to the DB and writes an upgrade/downgrade script.
    3. Run:  alembic upgrade head
       Alembic executes the migration against the database.
    4. The `alembic_version` table in your DB records which revision is applied.
"""

from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context

# ── Import our app's config and models ─────────────────────────────
from app.config import settings
from app.database import Base

# Import all models so Base.metadata is fully populated
from app.models import User  # noqa: F401

# ── Alembic Config object ─────────────────────────────────────────
config = context.config

# Override the sqlalchemy.url from alembic.ini with our .env value
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# Set up Python logging from the .ini file
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# This is the MetaData object that Alembic uses for autogenerate.
# It reads all table definitions registered on Base.
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """
    Run migrations in 'offline' mode.
    Generates SQL scripts without connecting to the database.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """
    Run migrations in 'online' mode.
    Connects to the database and applies changes directly.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
