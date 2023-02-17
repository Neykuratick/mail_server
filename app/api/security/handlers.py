from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm

from app.api.security.schemes import TokenScheme
from app.api.security.service import create_access_token
from app.api.security.service import verify_password
from app.api.users.crud import UsersCRUD
from app.core.config import settings

router = APIRouter(prefix='/security')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f'{settings.API_V1_URL}/security/token')


@router.post('/token', response_model=TokenScheme)
async def authenticate(
    form_data: OAuth2PasswordRequestForm = Depends(),
    users: UsersCRUD = Depends(UsersCRUD)
):
    user = await users.get_user(username=form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    valid_password = verify_password(form_data.password, user.hashed_password)
    if not valid_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    token = create_access_token(data={"sub": user.username})
    return TokenScheme(access_token=token)
