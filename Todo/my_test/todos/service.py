# tests/unit/test_user_service.py
import pytest
from unittest.mock import MagicMock
from my_app.todos.service import *
from my_app.todos.schemas import *

@pytest.fixture
def mock_repo():
    return MagicMock()

@pytest.fixture
def service(mock_repo):
    return TodoService(repo=mock_repo)

def test_create_user_suc(service, mock_repo):
    mock_repo.find_by_email.return_value = None
    mock_repo.save.return_value = 

    data = TodoItem(title="FastAPI 공부", description="CRUD 구현 연습", priority="high",due_date="2025-05-01")

    # When
    result = service.create_user(data)

    # Then
    assert result.id == 1
    assert result.email == "hong@test.com"
    mock_repo.save.assert_called_once_with(data)


def test_create_user_이메일_중복(service, mock_repo):
    # Given: 이미 존재하는 이메일
    mock_repo.find_by_email.return_value = UserResponse(id=1, name="기존유저", email="hong@test.com")

    data = UserCreate(name="홍길동", email="hong@test.com")

    # When / Then
    with pytest.raises(ValueError, match="이미 존재하는 이메일"):
        service.create_user(data)


def test_get_user_존재하지_않음(service, mock_repo):
    # Given
    mock_repo.find_by_id.return_value = None

    # When / Then
    with pytest.raises(ValueError, match="찾을 수 없습니다"):
        service.get_user(999)