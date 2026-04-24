# my_test/todos/test_service.py
import pytest
from datetime import date
from core.exceptions import NotFoundException, ConflictException
from user.models import User
from user.service import UserService
from unittest.mock import MagicMock
from user.schemas import UserRequest

@pytest.fixture
def mock_repo():
    return MagicMock()

@pytest.fixture
def service(mock_repo):
    return UserService(repository=mock_repo)

def test_creat_user_suc(service, mock_repo):
    mock_repo.find_by_email.return_value = None
    mock_repo.save_user.return_value = User(id=1, name="high", email="abcd@naver.com")

    request = UserRequest(id=1, password="abcd1234", name="high", email="abcd@naver.com")
    # When
    result = service.create_user(request)

    # Then
    assert result.id == 1
    mock_repo.save_user.assert_called_once_with(request)

def test_creat_user_fail(service, mock_repo):
    mock_repo.find_by_email.return_value = User(id=1, name="high", email="abcd@naver.com")
    # Given
    mock_repo.save_user.return_value = None
    request = UserRequest(id=1, password="abcd1234", name="high", email="abcd@naver.com")

    # When / Then
    with pytest.raises(ConflictException) as e:
        service.create_user(request)
    assert e.value.status_code == 409
    assert e.value.message == "이미 존재하는 이메일"

def test_get_user_suc(service, mock_repo):
    mock_repo.get_user.return_value = User(id=1, name="high", email="abcd@naver.com")

    # When
    result = service.get_user(1)

    # Then
    assert result.id == 1
    mock_repo.get_user.assert_called_once_with(1)

def test_get_user_fail(service, mock_repo):
    mock_repo.find_by_id.return_value = None
    # Given
    mock_repo.get_user.return_value = None
    request = UserRequest(id=1, password="abcd1234", name="high", email="abcd@naver.com")

    # When / Then
    with pytest.raises(NotFoundException) as e:
        service.get_user(999)
    assert e.value.status_code == 404
    assert e.value.message == "존재하지 않습니다. id: 999"

def test_delete_user_suc(service, mock_repo):
    mock_repo.delete_user.return_value = True
    user_id = 1

    # When
    result = service.delete_user(user_id)

    # Then
    mock_repo.delete_user.assert_called_once_with(user_id)

def test_delete_user_fail(service, mock_repo):
    # Given
    mock_repo.delete_user.return_value = False

    # When / Then
    with pytest.raises(NotFoundException) as e:
        service.delete_user(999)
    assert e.value.status_code == 404
    assert e.value.message == "존재하지 않습니다. id: 999"
