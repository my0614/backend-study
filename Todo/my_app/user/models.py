from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Index
from sqlalchemy.orm import relationship
from core.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("role.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    role = relationship("Role", back_populates="users")

    __table_args__ = (Index("ix_user_email", "email"),)
