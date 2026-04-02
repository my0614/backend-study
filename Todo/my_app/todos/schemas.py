# todos/schemas.py
from pydantic import BaseModel
from typing import List  

class TodoObject(BaseModel):
    title: str
    description: str
    priority: str
    due_date: str
    
class CreateTodoRequest(BaseModel):
    title: str
    description: str
    priority: str
    due_date: str

class TodoListRequest(BaseModel):
    is_completed: bool
    priority: str

class TodoRequest(BaseModel):
    id: int

class UpdateTodoRequest(BaseModel):
    is_completed: bool
    priority: str

class DeleteTodoRequest(BaseModel):
    id: int

class CreateTodoResponse(BaseModel):
    TodoObject
    
    class Config:
        from_attributes = True

class TodoListResponse(BaseModel):
    todos: List[TodoObject]
    
    class Config:
        from_attributes = True