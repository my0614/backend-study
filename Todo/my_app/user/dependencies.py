# todos/dependencies.py
from fastapi import Depends
from sqlalchemy.orm import Session
from my_app.core.database import get_db
from user.service import UserService
from user.repository import UserRepository
from fastapi.security import HTTPBearer

security = HTTPBearer()

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repository = UserRepository(db)
    return UserService(repository)