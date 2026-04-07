# todos/dependencies.py
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from my_app.user.repository import UserRepository
from my_app.user.service import UserService

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repository = UserRepository(db)
    return UserRepository(repository)