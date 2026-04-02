# todos/schemas.py
from enum import Enum
from datetime import date 
from pydantic import BaseModel
from typing import List, Optional

class TodoItem(BaseModel):
    title: str
    description: str
    priority: str
    due_date: date
    
    class Config:
        from_attributes = True
                      
class TodoList(BaseModel):
    Todolist: list[TodoItem]
    
    class Config:
        from_attributes = True
                                                                                                                                                    
class PriorityEnum(str, Enum):                                                                                                                                                                            
    low = "low"                                                                                                                                                                                           
    medium = "medium"                                                                                                                                                                                     
    high = "high"      
      
class CreateTodoRequest(BaseModel):
    todo: TodoItem

class TodoListRequest(BaseModel):
    is_completed: Optional[bool] = None
    priority: Optional[str] = None
    
class TodoRequest(BaseModel):
    id: int

class UpdateTodoRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    priority: Optional[str] = None

class CreateTodoResponse(BaseModel):
    todo: TodoItem
    
    class Config:
        from_attributes = True
        
class TodoResponse(BaseModel):
    todo: TodoItem
    
    class Config:
        from_attributes = True
        
class TodoListResponse(BaseModel):
    todolist: list[TodoItem]

    class Config:
        from_attributes = True
        
class UpdateTodoResponse(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[str] = None
    priority: Optional[PriorityEnum] = "medium"
    
    class Config:
        from_attributes = True
