from fastapi import APIRouter
from fastapi import Depends

from app.api.security.deps import get_current_user
from app.api.security.service import get_password_hash
from app.api.users.crud import UsersCRUD
from app.api.users.schemes import UserCreateScheme
from app.api.users.schemes import UserReadScheme

router = APIRouter(prefix='/users')


@router.post('/register', response_model=UserReadScheme)
async def register(user: UserCreateScheme, users: UsersCRUD = Depends(UsersCRUD)):
    user_dicted = user.dict(exclude={'password'})
    user_dicted['hashed_password'] = get_password_hash(user.password)

    return await users.create_user(**user_dicted)


@router.post('/me', response_model=UserReadScheme)
async def get_me(user: UserReadScheme = Depends(get_current_user)):
    return user
