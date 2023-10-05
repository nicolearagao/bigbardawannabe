import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from tracker.db.session import get_db, Base
from tracker.api.server import app

# Create an in-memory SQLite database for testing
@pytest.fixture(scope="session")
def test_db():
    SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal
    Base.metadata.drop_all(bind=engine)

# Override the get_db dependency with the test database session
@pytest.fixture(scope="session")
def override_get_db(test_db):
    def override():
        try:
            db = test_db()
            yield db
        finally:
            db.close()
    return override

# Create a TestClient instance using the app
@pytest.fixture(scope="session")
def test_client(override_get_db):
    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)
