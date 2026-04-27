from fastapi import Depends
from sqlalchemy.orm import Session
from core.database import get_db
from role.service import RoleService
from role.repository import RoleRepository

def get_role_service(db: Session = Depends(get_db)) -> RoleService:
    repository = RoleRepository(db)
    return RoleService(repository, db)
