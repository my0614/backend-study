# todos/repository.py
import bcrypt
import logging
from datetime import date
from datetime import datetime
from user.models import User
from sqlalchemy.orm import Session
from user.schemas import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def is_password_used(self, password: str) -> bool:                                                         
        users = self.db.query(User).all()                                                                      
        for user in users:                                                                                     
            if bcrypt.checkpw(password.encode('utf-8'), user.password):
                return True                                                                                    
        return False    
      
    def find_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email==email).first()
    
    def save_user(self,  request: UserRequest) -> UserReponse:
        if self.is_password_used(request.password):
            raise ValueError("이미 사용중인 비밀번호입니다.")
        hashed = bcrypt.hashpw(request.password.encode('utf-8'), bcrypt.gensalt()) 
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