from typing import Optional
from pydantic import BaseModel, EmailStr


class RegisterRequest(BaseModel):
	name: str
	email: EmailStr
	password: str


class RegisterResponse(BaseModel):
	message: str


class LoginRequest(BaseModel):
	email: EmailStr
	password: str


class LoginResponse(BaseModel):
	message: str
	token: Optional[str] = None

