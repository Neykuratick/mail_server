from typing import Generic
from typing import TypeVar

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base_model import Base
from app.db.dep import get_session

ModelType = TypeVar("ModelType", bound=Base)


class BaseCRUD(Generic[ModelType]):
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session
