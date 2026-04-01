
from fastapi import FastAPI
from database import engine, Base
import todos.models  # 모델을 임포트해야 Base가 인식한다
from todos.router import router as todos_router

# 테이블 생성 (이미 있으면 건너뜀)
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(todos_router)