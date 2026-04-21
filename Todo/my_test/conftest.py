# tests/conftest.py
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../my_app"))

import pytest
from main import app
from core.database import Base, get_db
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from fastapi.testclient import TestClient
from core.config import get_settings, Settings

def get_test_settings():
      return Settings(
          database_url="sqlite://",
          secret_key="test-secret-key-for-testing-only",
      )

engine = create_engine(get_test_settings().database_url, connect_args={"check_same_thread": False}, poolclass=StaticPool)
TestingSessionLocal = sessionmaker(bind=engine)

@pytest.fixture(autouse=True)
def setup_db():
    """각 테스트 전에 테이블 생성, 후에 삭제"""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def client(db):
    """운영 DB 대신 테스트 DB를 주입한 TestClient"""
    def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()