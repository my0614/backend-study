from fastapi import Query 
from fastapi import APIRouter, Depends
from my_app.user.service import UserService
from my_app.user.dependencies import get_user_service
from my_app.user.schemas import *

router = APIRouter(prefix="/user", tags=["user"])