# todos/schemas.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import date                                                                                                                                                                       
 
class CreateTodoRequest(BaseModel):
    title: str
    description: str
    priority: str
    due_date: str

class TodoRequest(BaseModel):
    id: int

class UpdateTodoRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    priority: Optional[str] = None

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
        
class UpdateTodoResponse(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    priority: Optional[str] = None
    
    class Config:
        from_attributes = True
