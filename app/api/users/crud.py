from sqlalchemy import select
from app.api.temp.crud import TempCRUD
from app.api.temp.models import Temp
from app.api.users.models import UserModel
from app.db.base_crud import BaseCRUD


class UsersCRUD(BaseCRUD):
    async def create_user(self, username: str, email: str, hashed_password: str) -> UserModel:
        user = UserModel(username=username, email=email, hashed_password=hashed_password)  # noqa
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_user(self, username: str) -> UserModel:
        sql = select(UserModel).where(UserModel.username == username)

        res = await self.session.execute(sql)
        return res.scalar_one_or_none()

    async def test(self, temp_crud: TempCRUD, username: str) -> Temp:
        """Example of mixing cruds together"""
        return await temp_crud.get_temp(username=username)
