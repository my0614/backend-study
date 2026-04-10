# todos/schemas.py
from enum import Enum
from datetime import date 
from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class OrmBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
        
class TodoItem(OrmBaseModel):
    user_id: int
    title: str 
    description: str
    priority: Optional[PriorityEnum] = "medium"
    due_date: date
    id: Optional[int] = None
     
class TodoList(OrmBaseModel):
    todolist: list[TodoItem] 
    
class TodoListRequest(OrmBaseModel):
    user_id: Optional[int] = None
    is_completed: Optional[bool] = None
    priority: Optional[PriorityEnum] = None

class UpdateTodoRequest(OrmBaseModel):
    user_id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    priority: Optional[PriorityEnum] = None