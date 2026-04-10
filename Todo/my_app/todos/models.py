from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date, DateTime 
from my_app.core.database import Base
from datetime import datetime

class Todo(Base):
    __tablename__ = "todos"  # DB 테이블 이름
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"),nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    is_completed = Column(Boolean, default=False)
    priority = Column(String, default='medium')
    due_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.now)