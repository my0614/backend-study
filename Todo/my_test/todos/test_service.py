# my_test/todos/test_service.py
import pytest
from unittest.mock import MagicMock
from my_app.todos.service import *
from my_app.todos.schemas import TodoItem

@pytest.fixture
def mock_repo():
    return MagicMock()

@pytest.fixture
def service(mock_repo):
    return TodoService(repo=mock_repo)


def test_create_todo_suc(service, mock_repo):
    # Given: 이메일 중복 없음
    #mock_repo.find_by_email.return_value = None
    mock_repo.save.return_value = TodoItem(title="FastAPI 공부", description="CRUD 구현 연습", priority="high", due_date="2025-05-01",id=2)

    data = TodoItem(title="홍길동", description="hong@test.com",priority="high",due_date="2026-04-06")

    # When
    result = service.create_user(data)

    # Then
    assert result.title == "홍길동"
    assert result.email == "hong@test.com"
    assert result.priority == "high"
    assert result.due_date == "2026-04-06"
    assert result.id == 8
    mock_repo.save.assert_called_once_with(data)


