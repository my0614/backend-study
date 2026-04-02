
import logging
from fastapi import FastAPI
from database import engine, Base
import todos.models  # 모델을 임포트해야 Base가 인식한다
from todos.router import router as todos_router

logging.basicConfig(level=logging.INFO)
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(todos_router)