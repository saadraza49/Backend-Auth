# 🔐 Backend-Auth

A robust **Authentication & Authorization** REST API built with Python, featuring JWT-based security, password hashing, role-based access, and a cloud PostgreSQL database.

---

## 🚀 Tech Stack

| Layer | Technology |
|---|---|
| Framework | [FastAPI](https://fastapi.tiangolo.com/) |
| ORM | [SQLAlchemy](https://www.sqlalchemy.org/) |
| Migrations | [Alembic](https://alembic.sqlalchemy.org/) |
| Password Hashing | [Bcrypt](https://pypi.org/project/bcrypt/) |
| JWT Tokens | [Python-Jose](https://python-jose.readthedocs.io/) |
| Database | [Neon PostgreSQL](https://neon.tech/) (serverless) |

---

## ✨ Features

- ✅ User registration with hashed passwords
- ✅ JWT access token generation on login
- ✅ Protected routes via OAuth2 Bearer token
- ✅ Token expiration & validation
- ✅ SQLAlchemy models with Alembic migrations
- ✅ Cloud-hosted PostgreSQL via Neon

---

## 📁 Project Structure
```
backend-auth/
├── app/
│   ├── main.py           # FastAPI app entry point
│   ├── database.py       # SQLAlchemy engine & session
│   ├── models.py         # Database models
│   ├── schemas.py        # Pydantic request/response schemas
│   ├── routers/
│   │   ├── auth.py       # /login endpoint
│   │   └── users.py      # /register & user endpoints
│   └── utils/
│       ├── hashing.py    # Bcrypt password hashing
│       └── jwt.py        # Token creation & verification
├── alembic/              # Database migrations
├── alembic.ini
├── requirements.txt
└── .env                  # Environment variables
```