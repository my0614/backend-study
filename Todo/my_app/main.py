from fastapi import FastAPI
from database import engine, Base
import todos.models
import user.models  # 모델을 임포트해야 Base가 인식한다
from user.router import router as user_router
from todos.router import router as todo_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router)
app.include_router(todo_router)