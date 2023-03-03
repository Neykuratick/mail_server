from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from app.db.base_model import Base
from app.db.mixins import TimeMixin


class PermissionTargetModel(TimeMixin, Base):
    __tablename__ = "permission_targets"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = Column(String, unique=True, nullable=False)
    human_name: Mapped[str] = Column(String)


class PermissionActionModel(TimeMixin, Base):
    __tablename__ = "permission_actions"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = Column(String, unique=True, nullable=False)
    human_name: Mapped[str] = Column(String)


class PermissionTargetsActions(TimeMixin, Base):
    __tablename__ = "permission_target_actions"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True, autoincrement=True)
    target_id: Mapped[int] = Column(
        Integer,
        ForeignKey("permission_targets.id", ondelete="CASCADE"),
        nullable=False,
    )
    action_id: Mapped[int] = Column(
        Integer,
        ForeignKey("permission_actions.id", ondelete="CASCADE"),
        nullable=False,
    )

    target = relationship("PermissionTargetModel", lazy="joined", viewonly=True)
    action = relationship("PermissionActionModel", lazy="joined", viewonly=True)

    __table_args__ = (UniqueConstraint("target_id", "action_id"),)
