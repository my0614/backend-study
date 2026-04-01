# todos/schemas.py
from pydantic import BaseModel

class CreateTodoRequest(BaseModel):
    name: str
    email: str

class TodoResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True  # SQLAlchemy 모델 → Pydantic 변환 허용