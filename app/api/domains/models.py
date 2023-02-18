from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from app.api.users.models import UserModel
from app.db.base_model import Base
from app.db.mixins import TimeMixin


class DomainModel(TimeMixin, Base):
    __tablename = "domains"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner: Mapped[UserModel] = relationship("UserModel", lazy="joined")
