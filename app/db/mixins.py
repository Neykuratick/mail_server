from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy.orm import declared_attr


class TimeMixin:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    created_at = Column(DateTime, default=datetime.utcnow)
