from pydantic import BaseModel

class OrmBaseModel(BaseModel):
    class Config:
        from_attributes = True

class LoginRequest(OrmBaseModel):
    email: str
    password: str

class TokenResponse(OrmBaseModel):
    access_token: str
    token_type: str = "bearer"