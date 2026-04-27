from pydantic import BaseModel, ConfigDict

class OrmBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class RoleRequest(OrmBaseModel):
    name: str

class RoleResponse(OrmBaseModel):
    id: int
    name: str
