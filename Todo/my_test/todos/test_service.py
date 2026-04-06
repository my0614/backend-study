# my_test/todos/test_service.py
import pytest
from datetime import date
from fastapi import HTTPException
from my_app.todos.service import *
from unittest.mock import MagicMock
from my_app.todos.schemas import TodoItem, TodoListRequest, UpdateTodoRequest

@pytest.fixture
def mock_repo():
    return MagicMock()

@pytest.fixture
def service(mock_repo):
    return TodoService(repository=mock_repo)

def test_create_todo_suc(service, mock_repo):
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


def test_get_todo_suc(service, mock_repo):
    mock_repo.get_todo.return_value = TodoItem(title="FastAPI 공부", description="CRUD 구현 연습", priority="high", due_date="2025-05-01",id=2)
    todo_id = 2
    # When
    result = service.get_todo(todo_id)

    # Then
    assert result.title == "FastAPI 공부"
    assert result.description == "CRUD 구현 연습"
    assert result.priority == "high"
    assert result.due_date == date(2025, 5, 1)
    assert result.id == 2
    mock_repo.get_todo.assert_called_once_with(todo_id)

def test_get_todo_fail(service, mock_repo):
    # Given
    mock_repo.get_todo.return_value = None

    # When / Then
    with pytest.raises(HTTPException, match="존재하지 않는 id") as e:
        service.get_user(999)
    assert e.value.status_code == 404

def test_get_all_todo_suc(service, mock_repo):
    todo1 = TodoItem(title="dfsdfdfsfd", description="CRUD 연습", priority="high",due_date="2026-04-03", id=6)
    todo2 = TodoItem(title="공부", description="FastAPI", priority="high", due_date="2026-04-10", id=1)
    mock_repo.get_todo_list.return_value = [todo1, todo2]
    request = TodoListRequest(is_completed=None, priority="high")
    
    # When
    result = service.get_all_todos(request)
    
    # Then
    assert len(result.todolist) == 2           # 리스트 길이 검증
    assert result.todolist[0].title == "dfsdfdfsfd"  # 첫번째 항목
    assert result.todolist[1].title == "공부"   # 두번째 항목
    mock_repo.get_todo_list.assert_called_once_with(request)


def test_update_todo_suc(service, mock_repo):
    mock_repo.update_todo.return_value = TodoItem(title="update test",id=6)
    request = UpdateTodoRequest(title="update test")
    todo_id = 6
    # When
    result = service.update_todo(todo_id, request)

    # Then
    assert result.title == "update test"
    assert result.id == todo_id
    mock_repo.update_todo.assert_called_once_with(todo_id, request)
