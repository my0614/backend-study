# app/core/exception_handlers.py
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from core.exceptions import AppException
from core.schemas import ErrorResponse

async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(code=exc.code, message=exc.message, detail=exc.detail).model_dump(),
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    detail = [
        {"field": ".".join(str(loc) for loc in e["loc"][1:]), "message": e["msg"]}
        for e in errors
    ]
    return JSONResponse(
        status_code=422,
        content=ErrorResponse(code="VALIDATION_ERROR", message="요청 데이터가 올바르지 않습니다", detail=detail).model_dump(),
    )

async def unhandled_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(code="INTERNAL_SERVER_ERROR", message="서버 내부 오류가 발생했습니다").model_dump(),
    )