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

# 테스트용 인메모리 SQLite DB
TEST_DATABASE_URL = "sqlite://"

engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool)
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
