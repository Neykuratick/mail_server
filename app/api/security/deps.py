import logging

from fastapi import Depends
from fastapi import HTTPException
from jose import ExpiredSignatureError
from jose import JWTError
from jose import jwt

from app.api.security.handlers import oauth2_scheme
from app.api.users.crud import UsersCRUD
from app.api.users.schemes import UserReadScheme
from app.core.config import settings


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    users: UsersCRUD = Depends(UsersCRUD),
) -> UserReadScheme:
    try:
        payload = jwt.decode(
            token=token,
            key=settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
        )
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except JWTError as e:
        logging.debug(f"JWT decoding error: {e}")
        raise HTTPException(status_code=401, detail="Could not decode JWT token")

    username = payload.get("sub")
    if username is None:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

    user = await users.get_user(username=username)
    if user is None:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

    return UserReadScheme.from_orm(user)
