# dependencies.py
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from auth.auth import decode_token

security = HTTPBearer()

def get_current_user_id(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> int:
    return decode_token(credentials.credentials)