from sqlalchemy import Column, Integer, String
from app.db.base_model import Base
from app.db.mixins import TimeMixin


class User(TimeMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
