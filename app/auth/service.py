import hashlib
import os
from typing import Dict

from .models import RegisterRequest, LoginRequest

# Simple in-memory user store. Keys are emails.
_USER_STORE: Dict[str, Dict] = {}


def _hash_password(password: str) -> str:
	"""Hash a password using PBKDF2-HMAC-SHA256 and a random salt.

	Stored format: salt$hexhash
	"""
	salt = os.urandom(16).hex()
	dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 100_000)
	return f"{salt}${dk.hex()}"


def _verify_password(password: str, stored: str) -> bool:
	try:
		salt, hexhash = stored.split("$")
	except ValueError:
		return False
	dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 100_000)
	return dk.hex() == hexhash


def register_user(req: RegisterRequest) -> bool:
	"""Register a new user.

	Returns True on success, False if the email already exists.
	"""
	email = req.email.lower()
	if email in _USER_STORE:
		return False

	hashed = _hash_password(req.password)
	user = {"name": req.name, "email": email, "password": hashed}
	_USER_STORE[email] = user
	return True


def login_user(req: LoginRequest) -> bool:
	"""Validate login credentials. Returns True if valid, False otherwise."""
	email = req.email.lower()
	user = _USER_STORE.get(email)
	if not user:
		return False
	stored = user.get("password")
	if not stored:
		return False
	return _verify_password(req.password, stored)


def get_user_by_email(email: str):
	return _USER_STORE.get(email.lower())

