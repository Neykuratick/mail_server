from typing import List

from fastapi import APIRouter
from fastapi import Form
from fastapi import Depends

from app.api.roles.crud import RolesCRUD
from app.api.roles.schemes import RoleScheme

router = APIRouter(prefix="/roles")


@router.post("", response_model=RoleScheme)
async def create_role(
    name: str = Form(),
    human_name: str = Form(),
    roles: RolesCRUD = Depends(RolesCRUD),
):
    return await roles.create_new_role(name=name, human_name=human_name)


@router.get("", response_model=List[RoleScheme])
async def get_roles(
    roles: RolesCRUD = Depends(RolesCRUD),
):
    return await roles.get_roles()
