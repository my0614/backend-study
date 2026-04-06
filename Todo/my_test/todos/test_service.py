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
    with pytest.raises(HTTPException, match="존재하지 않습니다. id: 999") as e:
        service.get_todo(999)
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
    mock_repo.update_todo.return_value = TodoItem(title="dfsdfdfsfd", description="CRUD 연습", priority="high",due_date="2026-04-03", id=6)
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
    todo_id=999
    # When / Then
    with pytest.raises(HTTPException, match="존재하지 않습니다. id: 999") as e:
        service.update_todo(todo_id, request)
    assert e.value.status_code == 404

def test_delete_todo_suc(service, mock_repo):
    mock_repo.delete_todo.return_value = True
    todo_id = 1
    # When
    result = service.delete_todo(todo_id)

    # Then
    mock_repo.delete_todo.assert_called_once_with(todo_id)
    
def test_delete_todo_fail(service, mock_repo):
    # Given
    mock_repo.delete_todo.return_value = False

    # When / Then
    with pytest.raises(HTTPException, match="999") as e:
        service.delete_todo(999)
    assert e.value.status_code == 404
    
def test_duedata_todo_suc(service, mock_repo):
    todo1 = TodoItem(title="호호잇", description="string", priority="medium", due_date="2026-01-01", id=4)
    todo2 = TodoItem(title="hello", description="", priority="high", due_date="2026-04-03", id=6)
    todo3 = TodoItem(title="test_code", description="string", priority="medium", due_date="2026-04-06", id=7)
    todo4 = TodoItem(title="string", description="string", priority="medium", due_date="2026-04-06", id=8)
    mock_repo.get_overdue_todo.return_value = [todo1, todo2, todo3, todo4]

    # When
    result = service.get_overdue_todo()

    # Then
    assert len(result.todolist) == 4
    assert result.todolist[0].title == "호호잇"
    assert result.todolist[1].title == "hello"
    assert result.todolist[2].title == "test_code"
    assert result.todolist[3].title == "string"
    mock_repo.get_overdue_todo.assert_called_once_with()
    
def test_duedata_todo_fail(service, mock_repo):
    # Given
    mock_repo.get_overdue_todo.return_value = None

    # When / Then
    with pytest.raises(HTTPException, match="존재하지 않습니다.") as e:
        service.get_overdue_todo()
    assert e.value.status_code == 404