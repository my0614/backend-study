# todos/repository.py
import logging
from datetime import date
from datetime import datetime
from my_app.user.models import User
from sqlalchemy.orm import Session
from my_app.user.schemas import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserRepository:
    def __init__(self, db: Session):
        self.db = db