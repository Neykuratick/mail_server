from typing import List
from typing import Optional

from sqlalchemy import or_
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.api.permissions.models import PermissionActionModel
from app.api.permissions.models import PermissionTargetModel
from app.api.permissions.models import PermissionTargetsActions
from app.db.base_crud import BaseCRUD
from app.exceptions.decorators import expect_arguments


class PermissionsCRUD(BaseCRUD[PermissionTargetsActions]):
    async def create_new_binding(self, target_id: int, action_id: int):
        target = await self.base_get(select(PermissionTargetModel.id).filter_by(id=target_id))
        action = await self.base_get(select(PermissionActionModel.id).filter_by(id=action_id))
        return await self.base_insert(
            table=PermissionTargetsActions,
            target_id=target,
            action_id=action,
        )

    async def get_bindings(self) -> List[PermissionTargetsActions]:
        stmt = select(PermissionTargetsActions).options(
            joinedload(PermissionTargetsActions.target), joinedload(PermissionTargetsActions.action)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all() or []

    @expect_arguments
    async def get_target(
        self,
        target_id: Optional[int] = None,
        target_name: Optional[str] = None,
    ) -> PermissionTargetModel:
        stmt = select(PermissionTargetModel).where(
            or_(
                PermissionTargetModel.id == target_id,
                PermissionTargetModel.name == target_name,
            )
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
