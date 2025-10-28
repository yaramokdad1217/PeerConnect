# 🎓 PeerConnect

PeerConnect is a web (FastAPI) and mobile-ready backend prototype that helps university students connect for study sessions, group projects, and peer tutoring. This repository contains the Sprint 1 authentication module (registration + login), unit and integration tests, and documentation for getting the project running locally.
---
**First sketch of PeerConnect sprint 1 UI pages:**
https://www.figma.com/make/jMnICis0nyWg0H3tTVv0bi/Student-Study-Collaboration-App?node-id=0-1&p=f&t=iQtfhFFNcazPFkcy-0&fullscreen=1

---

Table of contents
- [Overview](#overview)
- [Sprint 1 — Auth module](#sprint-1---auth-module)
  - [Features](#features)
  - [API endpoints](#api-endpoints)
  - [Request / Response examples](#request--response-examples)
  - [Security details](#security-details)
- [Repository structure](#repository-structure)
- [Requirements](#requirements)
- [Local setup](#local-setup)
- [Running the app](#running-the-app)
- [Running tests](#running-tests)
- [Development notes & recommended workflow](#development-notes--recommended-workflow)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Sprint 1 implements secure user registration and login endpoints using FastAPI. It uses best practices for password hashing and JWT-based authentication tokens so subsequent sprints can build on top of a secure auth foundation.

---

## Sprint 1 — Auth module

### Features
- User registration with name, email and password
- Login returning a JWT access token
- Password hashing (bcrypt)
- Pydantic request / response models with validation
- FastAPI endpoints and interactive OpenAPI docs
- Unit tests for service logic and integration tests for API routes

### API endpoints

Base path: `/auth` (mounted by `app/main.py`)

- POST `/auth/register`
  - Registers a new user.
  - Request body: name, email, password.
  - Response: created user object (no password) or error (email exists, validation errors).

- POST `/auth/login`
  - Authenticates a user and returns a JWT access token.
  - Request body: email, password.
  - Response: { "access_token": "<jwt>", "token_type": "bearer" } on success.

API docs (interactive):
- OpenAPI UI: GET /docs
- ReDoc: GET /redoc

> Note: If you change the mount path in `app/main.py`, update the URLs accordingly.

### Request / Response examples

Register example (curl):
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Example",
    "email": "alice@example.edu",
    "password": "S3cur3P@ssw0rd"
  }'
```

Successful register response (example):
```json
{
  "id": 1,
  "name": "Alice Example",
  "email": "alice@example.edu",
  "created_at": "2025-10-28T12:00:00Z"
}
```

Login example (curl):
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "alice@example.edu",
    "password": "S3cur3P@ssw0rd"
  }'
```

Successful login response (example):
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Security details

- Passwords must never be stored in plain text. Sprint 1 uses bcrypt (via passlib or bcrypt package) to hash and verify passwords.
- JWT tokens are used for stateless authentication. Provide a strong SECRET_KEY in environment variables.
- Recommended environment variables (described in Setup below):
  - SECRET_KEY — cryptographically secure secret for signing JWTs
  - ALGORITHM — JWT algorithm (e.g., HS256)
  - ACCESS_TOKEN_EXPIRE_MINUTES — token lifetime in minutes
  - DATABASE_URL — (optional) SQLite or other DB connection string

---

## Repository structure

Top-level (relevant files and folders):
- app/
  - auth/
    - controller.py — FastAPI endpoints (routes) for registration and login
    - service.py — Core auth business logic (register, authenticate) and password hashing
    - models.py — Pydantic request/response models
  - main.py — FastAPI app entrypoint that mounts auth routes
  - tests/
    - test_service.py — Unit tests for service layer
    - test_controller.py — Integration tests for the API routes
- requirements.txt — Python dependencies
- docs/ — design docs, diagrams, project proposal, and AI usage logs

(See the repo for full contents and diagrams inside docs/.)

---

## Requirements

- Python 3.9+ (3.10 recommended)
- pip (and virtualenv / venv)
- SQLite (default) or another database if you prefer (set DATABASE_URL)

Python packages are documented in `requirements.txt`. Typical dependencies for the auth sprint:
- fastapi
- uvicorn
- pydantic
- passlib[bcrypt] or bcrypt
- python-jose or PyJWT (for JWT creation/verification)
- pytest (for tests)
- httpx or requests (for integration tests)

---

## Local setup

1. Clone the repo
```bash
git clone https://github.com/yaramokdad1217/PeerConnect.git
cd PeerConnect
git checkout a556a6c7711236f8ee659e052f0ba6581f68f216
```

2. Create and activate a virtual environment
Unix/macOS:
```bash
python -m venv .venv
source .venv/bin/activate
```
Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Configure environment variables
Create a `.env` file at project root or export variables in your shell.

Example `.env` (recommended):
```
SECRET_KEY=replace_with_a_strong_random_value
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=sqlite:///./peerconnect.db
```

If you prefer exporting variables in the shell:
```bash
export SECRET_KEY="replace_with_a_strong_random_value"
export ALGORITHM="HS256"
export ACCESS_TOKEN_EXPIRE_MINUTES="60"
export DATABASE_URL="sqlite:///./peerconnect.db"
```

Notes:
- If DATABASE_URL is omitted, the project may default to an in-memory store or a local SQLite file depending on the implementation in `app/auth/service.py`.

---

## Running the app

Start the FastAPI backend using uvicorn:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open your browser:
- Interactive API docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

Test the auth endpoints (Register and Login) using curl, HTTPie, or the OpenAPI UI.

---

## Running tests

Run unit and integration tests with pytest:

```bash
pytest -q
```

If tests require environment variables, set them before running tests or ensure tests set defaults for CI.

---

## Development notes & recommended workflow

- Follow FastAPI patterns: keep validators in Pydantic models (models.py) and business logic in service.py. Keep controllers (routes) thin and focused on request/response and error handling.
- Use environment variables for secrets and configuration. Do not commit secrets to the repo.
- Consider adding automated checks:
  - Pre-commit hooks for formatting (black) and linting (flake8)
  - GitHub Actions for CI (pytest)
- If you add persistent storage beyond SQLite, include migrations (Alembic) and update docs.

---

## Roadmap (next steps beyond Sprint 1)
- Sprint 2: User profiles, skill tagging, and searching for peers
- Sprint 3: Study group management and invitations
- Sprint 4: Real-time messaging integration (WebSockets)
- Cross-cutting: Role-based access control, rate-limiting, and production-ready deployment
