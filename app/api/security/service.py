from datetime import datetime
from datetime import timedelta

from fastapi import HTTPException
from jose import jwt
from passlib.context import CryptContext

from app.api.security.schemes import TokenScheme
from app.api.users.crud import UsersCRUD
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            **{settings.SECRET_MEASUREMENT_UNIT: settings.SECRET_EXPIRATION_TIME}
        )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        claims=to_encode,
        key=settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM,
    )
    return encoded_jwt


async def authenticate(
    username: str,
    password: str,
    users: UsersCRUD,
):
    user = await users.get_user(username=username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    valid_password = verify_password(password, user.hashed_password)
    if not valid_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    token = create_access_token(data={"sub": user.username})
    return TokenScheme(access_token=token)
