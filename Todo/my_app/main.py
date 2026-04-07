from fastapi import FastAPI
from database import engine, Base
import my_app.user.models  # 모델을 임포트해야 Base가 인식한다
from my_app.user.router import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router)