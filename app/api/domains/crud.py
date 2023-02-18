from app.api.domains.models import DomainModel
from app.db.base_crud import BaseCRUD


class DomainsCRUD(BaseCRUD[DomainModel]):
    async def create(self, name: str, user_id: int) -> DomainModel:
        model = DomainModel(name=name, owner_id=user_id)  # noqa
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return model
