from typing import Generic
from typing import List
from typing import TypeVar

from fastapi import Depends
from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base_model import Base
from app.db.dep import get_session

ActualModel = TypeVar("ActualModel", bound=Base)
BaseModel = TypeVar("BaseModel", bound=Base)


class BaseCRUD(Generic[ActualModel]):
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session

    async def base_insert(self, table: BaseModel = None, **kwargs) -> ActualModel:
        model = table(**kwargs)
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return model

    async def base_get(self, stmt: Select) -> ActualModel:
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def base_get_list(self, stmt: Select) -> List[ActualModel]:
        result = await self.session.execute(stmt)
        return result.scalars().all() or []
