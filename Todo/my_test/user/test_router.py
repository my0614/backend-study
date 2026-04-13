import pytest


def get_token(client, email, password):
    response = client.post("/auth/login", json={"email": email, "password": password})
    return response.json()["access_token"]


def test_user_create(client):
    response = client.post("/user", json={
        "name": "홍길동",
        "email": "test@naver.com",
        "password": "password123"
    })

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "홍길동"
    assert data["email"] == "test@naver.com"
    assert "id" in data


def test_user_email_check(client):
    client.post("/user", json={"name": "기존유저", "email": "test@naver.com", "password": "password123"})

    response = client.post("/user", json={"name": "홍길동", "email": "test@naver.com", "password": "password456"})

    assert response.status_code == 409


def test_user_get(client):
    client.post("/user", json={"name": "홍길동", "email": "test@naver.com", "password": "password123"})
    token = get_token(client, "test@naver.com", "password123")

    response = client.get("/user", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert response.json()["name"] == "홍길동"


def test_user_get_not_found(client):
    client.post("/user", json={"name": "홍길동", "email": "test@naver.com", "password": "password123"})
    token = get_token(client, "test@naver.com", "password123")

    client.delete("/user", headers={"Authorization": f"Bearer {token}"})

    response = client.get("/user", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 404


def test_user_delete(client):
    client.post("/user", json={"name": "홍길동", "email": "test@naver.com", "password": "password123"})
    token = get_token(client, "test@naver.com", "password123")

    response = client.delete("/user", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert client.get("/user", headers={"Authorization": f"Bearer {token}"}).status_code == 404
