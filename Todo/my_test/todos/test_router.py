def get_token(client, email, password):
    response = client.post("/auth/login", json={"email": email, "password": password})
    return response.json()["access_token"]


def create_user_and_token(client):
    client.post("/user", json={"name": "홍길동", "email": "test@naver.com", "password": "password123"})
    token = get_token(client, "test@naver.com", "password123")
    return {"Authorization": f"Bearer {token}"}


def create_todo(client, headers):
    response = client.post("/todos", json={
        "user_id": 0,
        "title": "FastAPI 공부",
        "description": "CRUD 구현 연습",
        "priority": "high",
        "due_date": "2025-05-01"
    }, headers=headers)
    return response


def test_todo_create(client):
    headers = create_user_and_token(client)
    response = create_todo(client, headers)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "FastAPI 공부"
    assert data["description"] == "CRUD 구현 연습"
    assert data["priority"] == "high"
    assert "id" in data


def test_get_todo(client):
    headers = create_user_and_token(client)
    todo_id = create_todo(client, headers).json()["id"]

    response = client.get(f"/todos/{todo_id}", headers=headers)

    assert response.status_code == 200
    assert response.json()["title"] == "FastAPI 공부"


def test_get_todo_list(client):
    headers = create_user_and_token(client)
    create_todo(client, headers)

    response = client.get("/todos", headers=headers)

    assert response.status_code == 200
    assert len(response.json()["todolist"]) == 1


def test_update_todo(client):
    headers = create_user_and_token(client)
    todo_id = create_todo(client, headers).json()["id"]

    response = client.patch(f"/todos/{todo_id}", json={"title": "수정된 할일"}, headers=headers)

    assert response.status_code == 200
    assert response.json()["title"] == "수정된 할일"


def test_delete_todo(client):
    headers = create_user_and_token(client)
    todo_id = create_todo(client, headers).json()["id"]

    response = client.delete(f"/todos/{todo_id}", headers=headers)

    assert response.status_code == 204
    assert client.get(f"/todos/{todo_id}", headers=headers).status_code == 404
