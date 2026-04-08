# todos/repository.py
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
        
    def find_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email==email).first()
    
    def save_user(self,  request: UserRequest) -> UserReponse:
        user = User(id=request.id, password=request.password, name=request.name, email=request.email)
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