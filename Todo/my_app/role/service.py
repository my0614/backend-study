from role.models import Role
from role.repository import RoleRepository
from role.schemas import RoleRequest, RoleResponse
from core.exceptions import ConflictException, NotFoundException
from sqlalchemy.orm import Session

class RoleService:
    def __init__(self, repository: RoleRepository, db: Session):
        self.repository = repository
        self.db = db

    def create_role(self, request: RoleRequest) -> RoleResponse:
        if self.repository.find_by_name(request.name):
            raise ConflictException(message=f"이미 존재하는 역할입니다: {request.name}")
        role = Role(name=request.name)
        self.repository.save(role)
        self.db.commit()
        self.db.refresh(role)
        return role

    def get_or_create(self, name: str) -> Role:
        role = self.repository.find_by_name(name)
        if role is None:
            role = Role(name=name)
            self.repository.save(role)
        return role

    def get_role(self, id: int) -> RoleResponse:
        role = self.repository.find_by_id(id)
        if role is None:
            raise NotFoundException(message=f"존재하지 않습니다. id: {id}")
        return role
