from fastapi import FastAPI
from my_app.core.database import engine, Base
import todos.models
import user.models  # 모델을 임포트해야 Base가 인식한다
from user.router import router as user_router
from todos.router import router as todo_router
from auth.router import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router)
app.include_router(todo_router)
app.include_router(auth_router)