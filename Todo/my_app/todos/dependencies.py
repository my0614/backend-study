# todos/dependencies.py
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from my_app.todos.repository import TodoRepository
from my_app.todos.service import TodoService

def get_todo_service(db: Session = Depends(get_db)) -> TodoService:
    repository = TodoRepository(db)
    return TodoService(repository)