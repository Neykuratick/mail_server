from typing import List

from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends

from app.api.permissions.crud import PermissionsCRUD
from app.api.permissions.schemes import PermissionScheme

router = APIRouter(prefix="/permissions")


@router.post("/binding", response_model=PermissionScheme)
async def create_binding(
    target_id: int = Body(),
    action_id: int = Body(),
    permissions: PermissionsCRUD = Depends(PermissionsCRUD),
):
    return await permissions.create_new_binding(target_id=target_id, action_id=action_id)


@router.get("", response_model=List[PermissionScheme])
async def get_bindings(
    permissions: PermissionsCRUD = Depends(PermissionsCRUD),
):
    return await permissions.get_bindings()
