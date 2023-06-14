from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from tracker.db.models.user import User

def get_user(db: Session):
    """Placeholder while login is not implemented."""
    try:
        user = db.query(User).first()
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error_message)
    return user

