from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base

class Role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    users = relationship("User", back_populates="role")
