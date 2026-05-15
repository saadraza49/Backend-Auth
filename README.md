# 🔐 Backend-Authentication

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
└── .env                  # Environment variables (not committed)
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/backend-auth.git
cd backend-auth
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://user:password@your-neon-host/dbname
SECRET_KEY=your_super_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Run database migrations

```bash
alembic upgrade head
```

### 6. Start the server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

---

## 📡 API Endpoints

### Auth

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `POST` | `/register` | Register a new user | ❌ |
| `POST` | `/login` | Login and receive JWT | ❌ |

### Users

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/users/me` | Get current user info | ✅ Bearer Token |

---

## 🔑 Authentication Flow

```
1. POST /register  →  User created with hashed password
2. POST /login     →  Returns { access_token, token_type }
3. GET  /users/me  →  Pass token in Authorization: Bearer <token>
```

---

## 🧪 Interactive Docs

FastAPI provides auto-generated documentation:

- **Swagger UI** → `http://127.0.0.1:8000/docs`
- **ReDoc** → `http://127.0.0.1:8000/redoc`

---

## 🗄️ Database

This project uses **[Neon](https://neon.tech/)** — a serverless, cloud-hosted PostgreSQL provider. Schema changes are managed via **Alembic** migrations.

To create a new migration after modifying models:

```bash
alembic revision --autogenerate -m "describe your change"
alembic upgrade head
```

---

## 📦 Requirements

```
fastapi
uvicorn
sqlalchemy
alembic
bcrypt
python-jose[cryptography]
psycopg2-binary
python-dotenv
passlib
```

---

## 🛡️ Security Notes

- Passwords are **never stored in plain text** — Bcrypt hashing is applied before saving.
- JWTs are signed with a secret key and include an expiration timestamp.
- Always keep your `.env` file out of version control (add it to `.gitignore`).

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).