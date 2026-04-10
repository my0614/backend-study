# my_test/todos/test_service.py
import pytest
from datetime import date
from fastapi import HTTPException
from todos.service import *
from unittest.mock import MagicMock
from todos.schemas import TodoItem, TodoListRequest, UpdateTodoRequest

@pytest.fixture
def mock_repo():
    return MagicMock()

@pytest.fixture
def service(mock_repo):
    return TodoService(repository=mock_repo)

def test_create_todo_suc(service, mock_repo):
    mock_repo.save_todo.return_value = TodoItem(user_id=1, title="FastAPI 공부", description="CRUD 구현 연습", priority="high", due_date="2025-05-01", id=2)

    data = TodoItem(user_id=1, title="FastAPI 공부", description="CRUD 구현 연습", priority="high", due_date="2025-05-01")

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
    mock_repo.get_todo.return_value = TodoItem(user_id=1, title="FastAPI 공부", description="CRUD 구현 연습", priority="high", due_date="2025-05-01", id=2)
    todo_id = 2
    user_id = 1
    # When
    result = service.get_todo(todo_id, user_id)

    # Then
    assert result.title == "FastAPI 공부"
    assert result.description == "CRUD 구현 연습"
    assert result.priority == "high"
    assert result.due_date == date(2025, 5, 1)
    assert result.id == 2
    mock_repo.get_todo.assert_called_once_with(todo_id, user_id)

def test_get_todo_fail(service, mock_repo):
    # Given
    mock_repo.get_todo.return_value = None

    # When / Then
    with pytest.raises(HTTPException, match="존재하지 않습니다. id: 999") as e:
        service.get_todo(999, 1)
    assert e.value.status_code == 404

def test_get_all_todo_suc(service, mock_repo):
    todo1 = TodoItem(user_id=1, title="dfsdfdfsfd", description="CRUD 연습", priority="high", due_date="2026-04-03", id=6)
    todo2 = TodoItem(user_id=1, title="공부", description="FastAPI", priority="high", due_date="2026-04-10", id=1)
    mock_repo.get_todo_list.return_value = [todo1, todo2]
    request = TodoListRequest(is_completed=None, priority="high")

    # When
    result = service.get_all_todos(request)

    # Then
    assert len(result.todolist) == 2
    assert result.todolist[0].title == "dfsdfdfsfd"
    assert result.todolist[1].title == "공부"
    mock_repo.get_todo_list.assert_called_once_with(request)

def test_update_todo_suc(service, mock_repo):
    mock_repo.update_todo.return_value = TodoItem(user_id=1, title="dfsdfdfsfd", description="CRUD 연습", priority="high", due_date="2026-04-03", id=6)
    request = UpdateTodoRequest(title="update test")
    todo_id = 6
    # When
    result = service.update_todo(todo_id, request)

    # Then
    assert result.title == "dfsdfdfsfd"
    assert result.id == todo_id
    mock_repo.update_todo.assert_called_once_with(todo_id, request)

def test_update_todo_fail(service, mock_repo):
    # Given
    mock_repo.update_todo.return_value = None
    request = UpdateTodoRequest(title="update test")
    todo_id = 999
    # When / Then
    with pytest.raises(HTTPException, match="존재하지 않습니다. id: 999") as e:
        service.update_todo(todo_id, request)
    assert e.value.status_code == 404

def test_delete_todo_suc(service, mock_repo):
    mock_repo.delete_todo.return_value = True
    todo_id = 1
    user_id = 1
    # When
    result = service.delete_todo(todo_id, user_id)

    # Then
    mock_repo.delete_todo.assert_called_once_with(todo_id, user_id)

def test_delete_todo_fail(service, mock_repo):
    # Given
    mock_repo.delete_todo.return_value = False

    # When / Then
    with pytest.raises(HTTPException, match="999") as e:
        service.delete_todo(999, 1)
    assert e.value.status_code == 404

def test_duedata_todo_suc(service, mock_repo):
    todo1 = TodoItem(user_id=1, title="호호잇", description="string", priority="medium", due_date="2026-01-01", id=4)
    todo2 = TodoItem(user_id=1, title="hello", description="", priority="high", due_date="2026-04-03", id=6)
    todo3 = TodoItem(user_id=1, title="test_code", description="string", priority="medium", due_date="2026-04-06", id=7)
    todo4 = TodoItem(user_id=1, title="string", description="string", priority="medium", due_date="2026-04-06", id=8)
    mock_repo.get_overdue_todo.return_value = [todo1, todo2, todo3, todo4]
    user_id = 1

    # When
    result = service.get_overdue_todo(user_id)

    # Then
    assert len(result.todolist) == 4
    assert result.todolist[0].title == "호호잇"
    assert result.todolist[1].title == "hello"
    assert result.todolist[2].title == "test_code"
    assert result.todolist[3].title == "string"
    mock_repo.get_overdue_todo.assert_called_once_with(user_id)

def test_duedata_todo_fail(service, mock_repo):
    # Given
    mock_repo.get_overdue_todo.return_value = None

    # When / Then
    with pytest.raises(HTTPException, match="존재하지 않습니다.") as e:
        service.get_overdue_todo(1)
    assert e.value.status_code == 404

# user_id 체크 테스트
def test_get_todo_wrong_user(service, mock_repo):
    # Given: 다른 유저의 todo에 접근하면 repository가 None 반환
    mock_repo.get_todo.return_value = None

    # When / Then
    with pytest.raises(HTTPException) as e:
        service.get_todo(1, user_id=999)
    assert e.value.status_code == 404
    mock_repo.get_todo.assert_called_once_with(1, 999)

def test_update_todo_wrong_user(service, mock_repo):
    # Given: 다른 유저의 todo 수정 시 repository가 None 반환
    mock_repo.update_todo.return_value = None
    request = UpdateTodoRequest(user_id=999, title="update test")

    # When / Then
    with pytest.raises(HTTPException) as e:
        service.update_todo(1, request)
    assert e.value.status_code == 404
    mock_repo.update_todo.assert_called_once_with(1, request)

def test_delete_todo_wrong_user(service, mock_repo):
    # Given: 다른 유저의 todo 삭제 시 repository가 False 반환
    mock_repo.delete_todo.return_value = False

    # When / Then
    with pytest.raises(HTTPException) as e:
        service.delete_todo(1, user_id=999)
    assert e.value.status_code == 404
    mock_repo.delete_todo.assert_called_once_with(1, 999)
