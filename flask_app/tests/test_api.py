import pytest
import requests

# BASE_URL = "http://localhost:5000"
BASE_URL = "http://app:5000"

@pytest.fixture(scope="session")
def auth_token():
    payload = {
        "username": "admin",
        "password": "password"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 200
    return response.json()["token"]

@pytest.fixture
def auth_headers(auth_token):
    return {"Authorization": f"Bearer {auth_token}"}

def test_login_success():
    payload = {"username": "admin", "password": "password"}
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 200
    assert "token" in response.json()

def test_login_failure():
    payload = {"username": "wrong", "password": "creds"}
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 401
    assert response.json()["message"] == "Invalid credentials"

def test_create_user_authorized(auth_headers):
    user_payload = {"name": "Test User", "email": "test@example.com"}
    response = requests.post(f"{BASE_URL}/users", json=user_payload, headers=auth_headers)
    assert response.status_code == 201
    assert response.json()["name"] == "Test User"

def test_create_user_unauthorized():
    user_payload = {"name": "Unauthorized User", "email": "bad@example.com"}
    response = requests.post(f"{BASE_URL}/users", json=user_payload)
    assert response.status_code == 401
    assert "message" in response.json()

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_invalid_token():
    headers = {"Authorization": "Bearer invalidtoken"}
    user_payload = {"name": "Bad Token", "email": "bad@token.com"}
    response = requests.post(f"{BASE_URL}/users", json=user_payload, headers=headers)
    assert response.status_code == 401
    assert "message" in response.json()
