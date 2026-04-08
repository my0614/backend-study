# todos/dependencies.py
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from todos.repository import TodoRepository
from todos.service import TodoService

def get_todo_service(db: Session = Depends(get_db)) -> TodoService:
    repository = TodoRepository(db)
    return TodoService(repository)