import logging
from user.models import User
from fastapi import HTTPException
from user.repository import *
from user.schemas import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
    
    def create_user(self, request: UserRequest) -> UserReponse:
        existing = self.repository.find_by_email(request.email)
        if existing:
            raise ValueError("이미 존재하는 이메일")
        user = self.repository.save_user(request)
        return UserReponse(user)
    
    def get_user(self, id: int) -> UserReponse:
        user = self.repository.get_user(id)
        if user is None:
            raise ValueError(f"존재하지 않습니다. id: {id}")
        return UserReponse(user)
        
    def delete_user(self, id: int) -> None:
        user = self.repository.delete_user(id)
        if user == False:
            raise HTTPException(status_code=404, detail=f"존재하지 않습니다. id: {id}")
