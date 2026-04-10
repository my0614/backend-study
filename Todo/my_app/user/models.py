from sqlalchemy import Column, Integer, String, DateTime 
from my_app.core.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "user"  # DB 테이블 이름
    id = Column(Integer, primary_key=True, index=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    