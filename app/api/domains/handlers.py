from fastapi import APIRouter
from fastapi import Depends

from app.api.domains.crud import DomainsCRUD
from app.api.domains.schemas import DomainCreateScheme
from app.api.domains.schemas import DomainReadScheme
from app.api.security.deps import get_current_user
from app.api.users.schemes import UserReadScheme

router = APIRouter(prefix="/domains")


@router.post("/create", response_model=DomainReadScheme)
async def create(
    domain: DomainCreateScheme,
    domains: DomainsCRUD = Depends(DomainsCRUD),
    user: UserReadScheme = Depends(get_current_user),
):
    return await domains.create(name=domain.name, user_id=user.id)
