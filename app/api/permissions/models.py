from sqlalchemy import Column
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped

from app.api.permissions.enums import ActionsEnm
from app.api.permissions.enums import TargetsEnum
from app.db.base_model import Base
from app.db.mixins import TimeMixin


class PermissionTargets(TimeMixin, Base):
    __tablename__ = "permission_targets"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = Column(Enum(TargetsEnum), unique=True, nullable=False)
    human_name: Mapped[str] = Column(String)


class PermissionActions(TimeMixin, Base):
    __tablename__ = "permission_actions"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = Column(Enum(ActionsEnm), unique=True, nullable=False)
    human_name: Mapped[str] = Column(String)


class PermissionTargetsActions(TimeMixin, Base):
    __tablename__ = "permission_target_actions"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True, autoincrement=True)
    target: Mapped[int] = Column(
        Integer,
        ForeignKey("permission_targets.id", ondelete="CASCADE"),
        nullable=False,
    )
    actions: Mapped[int] = Column(
        Integer,
        ForeignKey("permission_actions.id", ondelete="CASCADE"),
        nullable=False,
    )
