# todos/schemas.py
from pydantic import BaseModel
from typing import List
from datetime import date                                                                                                                                                                       
 
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
    title: str
    description: str
    priority: str
    due_date: date
    
    class Config:
        from_attributes = True
        
class TodoResponse(BaseModel):
    title: str
    description: str
    priority: str
    due_date: date
    
    class Config:
        from_attributes = True