import todos.models
import user.models
from fastapi import FastAPI
from core.database import engine, Base
from core.exceptions import AppException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from core.exception_handlers import (
    app_exception_handler,
    validation_exception_handler,
    unhandled_exception_handler,
)

from user.router import router as user_router
from todos.router import router as todo_router
from auth.router import router as auth_router

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
      CORSMiddleware,
allow_origins=["http://localhost:3000"], # 프론트엔드 주소
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

app.include_router(user_router)
app.include_router(todo_router)
app.include_router(auth_router)