# todos/dependencies.py
from fastapi import Depends
from sqlalchemy.orm import Session
from core.database import get_db
from user.service import UserService
from user.repository import UserRepository
from role.repository import RoleRepository
from role.service import RoleService

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repository = UserRepository(db)
    role_service = RoleService(RoleRepository(db), db)
    return UserService(repository, role_service, db)