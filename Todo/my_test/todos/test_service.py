# my_test/todos/test_service.py
import pytest
from datetime import date
from my_app.todos.service import *
from unittest.mock import MagicMock
from my_app.todos.schemas import TodoItem

@pytest.fixture
def mock_repo():
    return MagicMock()

@pytest.fixture
def service(mock_repo):
    return TodoService(repository=mock_repo)

def test_create_todo_suc(service, mock_repo):
    # Given: 이메일 중복 없음
    #mock_repo.find_by_email.return_value = None
    mock_repo.save_todo.return_value = TodoItem(title="FastAPI 공부", description="CRUD 구현 연습", priority="high", due_date="2025-05-01",id=2)

    data = TodoItem(title="FastAPI 공부", description="CRUD 구현 연습", priority="high", due_date="2025-05-01")

    # When
    result = service.create_todo(data)

    # Then
    assert result.title == "FastAPI 공부"
    assert result.description == "CRUD 구현 연습"
    assert result.priority == "high"
    assert result.due_date == date(2025, 5, 1)
    assert result.id == 2
    mock_repo.save_todo.assert_called_once_with(data)


