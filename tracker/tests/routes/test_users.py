import pytest
from unittest import mock

from sqlalchemy import create_engine
from sqlalchemy.exc import MultipleResultsFound
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from tracker.db.session import get_db, Base
from tracker.api.server import app
from tracker.api.routes import users

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


class QueryMock:
    def __init__(self, raise_exception=False, return_value=False):
        ...

    def __call__(self):
        return self

    def query(self):
        return self

    def filter(self):
        return self

    def one_or_none(self):
        if raise_exception:
            raise MultipleResultsFound

def test_create_and_retrieve_user():
    something = QueryMock(...)
    # Ensure the database is empty before running the test
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    with TestClient(app) as client:
        response = client.post(
            "/api/users/",
            json={"username": "shadowman", "password": "Chimichangas10"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == "shadowman"

        response = client.post(
            "/api/users/",
            json={"username": "shadowman", "password": "Chimichangas20"},
        )
        assert response.status_code == 400


        with mock.patch.object('users.db', QueryMock()) as mock_query:
            mock_query.return_value.filter.return_value.one.side_effect = MultipleResultsFound
            response = client.post(
                "/api/users/",
                json={"username": "shadowman", "password": "Chimichangas30"},
            )
            assert response.status_code == 500
            assert "Multiple users with the same username found" in response.text

        # Test case 4: Missing username or password in the request
        response = client.post("/api/users/", json={})
        assert response.status_code == 422
# from unittest import mock
# from sqlalchemy.orm import Session
# from api.database import get_db
# from api.models import UserSchema
# from api.users import check_existing_user, create_user_endpoint

# def test_create_and_retrieve_user():
#     # Ensure the database is empty before running the test
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)

#     with TestClient(app) as client:
#         response = client.post(
#             "/api/users/",
#             json={"username": "shadowman", "password": "Chimichangas10"},
#         )
#         assert response.status_code == 200
#         data = response.json()
#         assert data["username"] == "shadowman"

#         response = client.post(
#             "/api/users/",
#             json={"username": "shadowman", "password": "Chimichangas20"},
#         )
#         assert response.status_code == 400

#         with mock.patch('users.check_existing_user') as mock_check_existing_user:
#             # Configure the mock behavior
#             mock_check_existing_user.return_value = True

#             response = client.post(
#                 "/api/users/",
#                 json={"username": "shadowman", "password": "Chimichangas30"},
#             )
#             assert response.status_code == 500
#             assert "Multiple users with the same username found" in response.text

#         # Test case 4: Missing username or password in the request
#         response = client.post("/api/users/", json={})
#         assert response.status_code == 422
