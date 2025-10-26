from fastapi import APIRouter, HTTPException, status

from .models import (
	RegisterRequest,
	RegisterResponse,
	LoginRequest,
	LoginResponse,
)
from .service import register_user, login_user

router = APIRouter()


@router.post("/register", response_model=RegisterResponse)
async def register(payload: RegisterRequest):
	"""Register a new user.

	Calls `service.register_user` which returns True on success or False if the
	email already exists.
	"""
	ok = register_user(payload)
	if not ok:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST, detail="email already registered"
		)

	return RegisterResponse(message="Registration successful")


@router.post("/login", response_model=LoginResponse)
async def login(payload: LoginRequest):
	"""Log in a user.

	Calls `service.login_user` which returns True for valid credentials.
	Returns 401 when credentials are invalid.
	"""
	ok = login_user(payload)
	if not ok:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid credentials"
		)

	return LoginResponse(message="Login successful", token=None)

