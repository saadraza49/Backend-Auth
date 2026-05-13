"""
FastAPI Application Entry Point
────────────────────────────────
Production-style authentication backend.

Run with:
    uvicorn app.main:app --reload

Swagger docs:
    http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import auth_router, users_router

# ── App Instance ────────────────────────────────────────────────────
app = FastAPI(
    title="FastAPI Auth Backend",
    description=(
        "A production-style authentication API built with "
        "FastAPI, PostgreSQL, SQLAlchemy 2.0, and JWT."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ── CORS Middleware ─────────────────────────────────────────────────
# In production, replace "*" with your frontend origin(s).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Register Routers ───────────────────────────────────────────────
app.include_router(auth_router)
app.include_router(users_router)


# ── Root Redirect ──────────────────────────────────────────────────
@app.get("/", include_in_schema=False)
def root():
    return {
        "message": "FastAPI Auth Backend is running"
    }
