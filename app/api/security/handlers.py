from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm

from app.api.security.schemes import TokenScheme
from app.api.security.service import authenticate
from app.api.users.crud import UsersCRUD
from app.core.config import settings

router = APIRouter(prefix="/security")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_URL}/security/token")


@router.post("/token", response_model=TokenScheme)
async def get_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    users: UsersCRUD = Depends(UsersCRUD),
):
    return await authenticate(
        password=form_data.password,
        username=form_data.username,
        users=users,
    )
