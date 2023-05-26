from sqlalchemy import Column, String

from tracker.db.base import BaseMixin
from tracker.db.session import Base

class User(Base, BaseMixin):
    __tablename__ = "user"

    username = Column(String, unique=True)
    password = Column(String)
