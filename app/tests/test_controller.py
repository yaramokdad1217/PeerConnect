from fastapi.testclient import TestClient
from app.main import app
from app.auth import service

client = TestClient(app)


def setup_function():
    # Clear in-memory store before each test
    service._USER_STORE.clear()


def test_register_success():
    payload = {"name": "Alice", "email": "alice@example.com", "password": "secret"}
    r = client.post("/auth/register", json=payload)
    assert r.status_code == 200
    assert r.json() == {"message": "Registration successful"}


def test_register_duplicate():
    payload = {"name": "Bob", "email": "bob@example.com", "password": "pwd"}
    r1 = client.post("/auth/register", json=payload)
    assert r1.status_code == 200
    r2 = client.post("/auth/register", json=payload)
    assert r2.status_code == 400


def test_login_success():
    reg = {"name": "Carol", "email": "carol@example.com", "password": "s3cr3t"}
    client.post("/auth/register", json=reg)
    login = {"email": reg["email"], "password": reg["password"]}
    r = client.post("/auth/login", json=login)
    assert r.status_code == 200
    assert r.json() == {"message": "Login successful", "token": None}


def test_login_wrong_password():
    reg = {"name": "Dan", "email": "dan@example.com", "password": "letmein"}
    client.post("/auth/register", json=reg)
    login = {"email": reg["email"], "password": "wrong"}
    r = client.post("/auth/login", json=login)
    assert r.status_code == 401
