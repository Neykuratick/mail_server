from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped

from app.db.base_model import Base
from app.db.mixins import TimeMixin


class Roles(TimeMixin, Base):
    __tablename__ = "roles"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = Column(String, unique=True, nullable=False)
    human_name: Mapped[str] = Column(String)


class RolesTargetActions(TimeMixin, Base):
    __tablename__ = "roles_target_actions"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True, autoincrement=True)
    role: Mapped[int] = Column(
        Integer,
        ForeignKey("roles.id", ondelete="CASCADE"),
        nullable=False,
    )
    target_action: Mapped[int] = Column(
        Integer,
        ForeignKey("permission_target_actions.id", ondelete="CASCADE"),
        nullable=False,
    )