# todos/schemas.py
from enum import Enum
from datetime import date
from pydantic import BaseModel, ConfigDict, field_validator
from typing import List, Optional, Any

class OrmBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
        
class UserRequest(OrmBaseModel):
    id: Optional[int] = None
    password: str
    name: str
    email: str
    role: str = "user"

class UserReponse(OrmBaseModel):
    id: int
    name: str
    email: str
    role: Optional[str] = None

    @field_validator("role", mode="before")
    @classmethod
    def extract_role_name(cls, v: Any) -> Optional[str]:
        if hasattr(v, "name"):
            return v.name
        return v
    