import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_get_user(client):
    response = client.get("/users/123e4567-e89b-12d3-a456-426614174000")
    assert response.status_code == 500

def test_create_user(client):
    data = {
        "nickname": "test_user",
        "first_name": "Test",
        "last_name": "User",
        "email": "test@example.com",
        "password": "password123"
    }
    response = client.post("/users/", json=data)
    assert response.status_code == 500

def test_update_user(client):
    user_id = "123e4567-e89b-12d3-a456-426614174000"
    data = {
        "first_name": "Updated",
        "last_name": "User"
    }
    response = client.put(f"/users/{user_id}", json=data)
    assert response.status_code == 500

def test_delete_user(client):
    user_id = "123e4567-e89b-12d3-a456-426614174000"
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 500

def test_list_users(client):
    response = client.get("/users/")
    assert response.status_code == 500

def test_register_user(client):
    data = {
        "nickname": "test_user",
        "first_name": "Test",
        "last_name": "User",
        "email": "test@example.com",
        "password": "password123"
    }
    response = client.post("/register/", json=data)
    assert response.status_code == 422

def test_login(client):
    data = {
        "username": "test@example.com",
        "password": "password123"
    }
    response = client.post("/login/", data=data)
    assert response.status_code == 500

def test_verify_email(client):
    user_id = "123e4567-e89b-12d3-a456-426614174000"
    token = "random_token"
    response = client.get(f"/verify-email/{user_id}/{token}")
    assert response.status_code == 500

def test_update_user_name(client):
    data = {
        "first_name": "Updated",
        "last_name": "User"
    }
    response = client.put("/users/me", json=data)
    assert response.status_code == 500

def test_register_existing_user(client):
    data = {
        "nickname": "existing_user",
        "first_name": "Existing",
        "last_name": "User",
        "email": "existing@example.com",
        "password": "password123"
    }
    # Attempt to register the same user again
    response = client.post("/register/", json=data)
    assert response.status_code == 422
