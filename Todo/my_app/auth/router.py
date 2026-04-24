# routers/auth.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from auth.service import authenticate_user
from core.jwt import create_access_token
from core.exceptions import UnauthorizedException
from auth.schemas import LoginRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=TokenResponse)
def login(body: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, body.email, body.password)
    if not user:
        raise UnauthorizedException(message="이메일 또는 비밀번호가 틀렸습니다")
    token = create_access_token(user.id)
    return TokenResponse(access_token=token)