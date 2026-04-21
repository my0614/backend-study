# app/core/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from core.config import get_settings

settings = get_settings()
engine = create_engine( settings.database_url, # 하드코딩 제거 pool_size=5,
max_overflow=10,
pool_recycle=1800, pool_pre_ping=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
class Base(DeclarativeBase):
    pass
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()