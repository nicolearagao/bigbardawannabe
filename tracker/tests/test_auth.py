import pytest 

from fastapi import HTTPException, status
from tracker.api.auth.authentication import get_user

class TestGetUser:
    def test_get_user_success(self, mocker):
        db_session = mocker.Mock()
        user = mocker.Mock()
        user.username = "shadowman"
        user.password = "12345"
        
        db_session.query.return_value.first.return_value = user
        result = get_user(db_session)
        assert result == user

    def test_get_user_error(self, mocker):
        db_session = mocker.Mock()
        db_session.query.side_effect = Exception("Database error")
        
        with pytest.raises(HTTPException) as error:
            get_user(db_session)

        assert error.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert "An error occurred" in error.value.detail





