from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from app.db.base_model import Base
from app.db.mixins import TimeMixin


class UserModel(TimeMixin, Base):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username: Mapped[str] = Column(String, unique=True, index=True)
    email: Mapped[str] = Column(String, unique=True, index=True)
    hashed_password: Mapped[str] = Column(String)

    def __str__(self):
        return self.username
