import pytest
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.db_models import Base
from fastapi.testclient import TestClient


@pytest.fixture
def test_client():
    client = TestClient(app)
    return client


@pytest.fixture(scope="module")
def test_db():
    _DB_URL = "sqlite://"

    engine = create_engine(
        _DB_URL, connect_args={"check_same_thread": False}
    )
    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )

    Base.metadata.create_all(bind=engine)

    try:
        db = TestingSessionLocal()
        yield db

    finally:
        db.close()
