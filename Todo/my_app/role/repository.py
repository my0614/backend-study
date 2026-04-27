from sqlalchemy.orm import Session
from role.models import Role

class RoleRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_name(self, name: str) -> Role | None:
        return self.db.query(Role).filter(Role.name == name).first()

    def find_by_id(self, id: int) -> Role | None:
        return self.db.query(Role).filter(Role.id == id).first()

    def save(self, role: Role) -> None:
        self.db.add(role)
