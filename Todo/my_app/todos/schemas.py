# todos/schemas.py
from pydantic import BaseModel

class CreateTodoRequest(BaseModel):
    title: str
    description: str
    priority: str
    due_date: str

class TodoListResponse(BaseModel):
    is_completed: bool
    priority: str

    class Config:
        from_attributes = True  # SQLAlchemy 모델 → Pydantic 변환 허용