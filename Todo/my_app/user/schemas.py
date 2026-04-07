# todos/schemas.py
from enum import Enum
from datetime import date 
from pydantic import BaseModel
from typing import List, Optional

class OrmBaseModel(BaseModel):
    class Config:
        from_attributes = True
        
class UserRequest(OrmBaseModel):
    id: Optional[int] = None
    password: str
    name: str
    email : str

class UserReponse(OrmBaseModel):
    id: int
    name: str
    email : str
    