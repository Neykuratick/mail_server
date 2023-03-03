from sqlalchemy import select

from app.api.domains.models import DomainModel
from app.db.base_crud import BaseCRUD


class DomainsCRUD(BaseCRUD[DomainModel]):
    async def create(self, name: str, user_id: int) -> DomainModel:
        return await self.base_insert(name=name, owner_id=user_id)

    async def get_by_id(self, domain_id: int) -> DomainModel:
        stmt = select(DomainModel).where(DomainModel.id == domain_id)
        query = await self.session.execute(stmt)
        return query.scalar_one_or_none()
