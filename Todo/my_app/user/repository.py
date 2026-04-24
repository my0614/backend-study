# todos/repository.py
import logging
from user.schemas import *
from user.models import User
from sqlalchemy.orm import Session
from core.exceptions import ConflictException
from core.security import hash_password, verify_password

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def authenticate_user(self, email: str, password: str) -> User | None:
        user = self.db.query(User).filter(User.email == email).first()
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

    def is_password_used(self, password: str) -> bool:
        hashed_passwords = self.db.query(User.password).all()
        return any(verify_password(password, row.password) for row in hashed_passwords)    
    
    def find_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email==email).first()
    
    def save_user(self,  request: UserRequest) -> UserReponse:
        if self.is_password_used(request.password):
            raise ConflictException(message="이미 사용중인 비밀번호입니다.")
        hashed = hash_password(request.password)
        user = User(password=hashed, name=request.name, email=request.email)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_user(self, id: int) -> UserReponse:
        return self.db.query(User).filter(User.id == id).first()

    def delete_user(self, id: int) -> bool:
        user = self.db.query(User).filter(User.id == id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        else:
            return False