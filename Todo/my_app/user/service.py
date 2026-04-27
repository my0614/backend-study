import logging
from user.schemas import *
from user.models import User
from user.repository import UserRepository
from role.service import RoleService
from core.exceptions import *
from core.security import hash_password
from sqlalchemy.orm import Session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserService:
    def __init__(self, repository: UserRepository, role_service: RoleService, db: Session):
        self.repository = repository
        self.role_service = role_service
        self.db = db

    def create_user(self, request: UserRequest) -> UserReponse:
        if self.repository.find_by_email(request.email):
            raise ConflictException(message="이미 존재하는 이메일")
        if self.repository.is_password_used(request.password):
            raise ConflictException(message="이미 사용중인 비밀번호입니다.")
        role = self.role_service.get_or_create(request.role)
        user = User(password=hash_password(request.password), name=request.name, email=request.email, role=role)
        self.repository.save_user(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user(self, id: int) -> UserReponse:
        user = self.repository.get_user(id)
        if user is None:
            raise NotFoundException(message=f"존재하지 않습니다. id: {id}")
        return user

    def delete_user(self, id: int) -> None:
        user = self.repository.delete_user(id)
        if user is None:
            raise NotFoundException(message=f"존재하지 않습니다. id: {id}")
        self.db.commit()
