import logging
from my_app.user.models import User
from fastapi import HTTPException
from my_app.user.repository import *
from my_app.user.schemas import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository