# todos/schemas.py
from enum import Enum
from datetime import date 
from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class OrmBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
        
class UserRequest(OrmBaseModel):
    id: Optional[int] = None
    password: str
    name: str
    email : str

class UserReponse(OrmBaseModel):
    id: int
    name: str
    email : str
    