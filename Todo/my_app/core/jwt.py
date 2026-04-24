# app/core/jwt.py
from datetime import datetime, timedelta
from jose import jwt, JWTError
from core.config import get_settings
from core.exceptions import UnauthorizedException

def create_access_token(user_id: int) -> str:
    settings = get_settings()
    expire = datetime.utcnow() + timedelta(
        minutes=settings.access_token_expire_minutes
    )
    payload = {"sub": str(user_id), "exp": expire}
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)

def decode_token(token: str) -> int:
      settings = get_settings()
      try:
          payload = jwt.decode(
              token, settings.secret_key, algorithms=[settings.algorithm])
          return int(payload["sub"])
      except JWTError:
          raise UnauthorizedException(message="유효하지 않은 토큰")
