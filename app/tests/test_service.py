from app.auth import service
from app.auth.models import RegisterRequest, LoginRequest


def setup_function():
	# Clear in-memory store before each test
	service._USER_STORE.clear()


def test_register_new_user_returns_true():
	req = RegisterRequest(name="Alice", email="alice@example.com", password="secret")
	assert service.register_user(req) is True
	assert service.get_user_by_email("alice@example.com") is not None


def test_register_duplicate_returns_false():
	req = RegisterRequest(name="Bob", email="bob@example.com", password="hunter2")
	assert service.register_user(req) is True
	# second attempt with same email should return False
	assert service.register_user(req) is False


def test_login_correct_credentials_returns_true():
	reg = RegisterRequest(name="Carol", email="carol@example.com", password="s3cr3t")
	assert service.register_user(reg) is True
	login = LoginRequest(email=reg.email, password=reg.password)
	assert service.login_user(login) is True


def test_login_wrong_password_returns_false():
	reg = RegisterRequest(name="Dan", email="dan@example.com", password="letmein")
	assert service.register_user(reg) is True
	login = LoginRequest(email=reg.email, password="wrongpassword")
	assert service.login_user(login) is False

