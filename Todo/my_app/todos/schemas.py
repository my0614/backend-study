# todos/schemas.py
from enum import Enum
from datetime import date 
from pydantic import BaseModel
from typing import List, Optional

class PriorityEnum(str, Enum):                                                                                                                                                                            
    low = "low"                                                                                                                                                                                           
    medium = "medium"                                                                                                                                                                                     
    high = "high"    

class OrmBaseModel(BaseModel):
    class Config:
        from_attributes = True
        
class TodoItem(OrmBaseModel):
    title: str
    description: str
    priority: Optional[PriorityEnum] = "medium"
    due_date: date
    id: int
     
class TodoList(OrmBaseModel):
    todolist: list[TodoItem] 
    
class TodoListRequest(OrmBaseModel):
    is_completed: Optional[bool] = None
    priority: Optional[PriorityEnum] = None

class UpdateTodoRequest(OrmBaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    priority: Optional[PriorityEnum] = None