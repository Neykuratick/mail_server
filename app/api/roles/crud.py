from typing import List

from sqlalchemy import select

from app.api.roles.models import RoleModel
from app.db.base_crud import BaseCRUD


class RolesCRUD(BaseCRUD[RoleModel]):
    async def create_new_role(self, name: str, human_name: str):
        return await self.base_insert(
            table=RoleModel,
            name=name,
            human_name=human_name,
        )

    async def get_roles(self) -> List[RoleModel]:
        return await self.base_get_list(select(RoleModel))