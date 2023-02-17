from sqlalchemy import text

from app.api.temp.models import Temp
from app.db.base_crud import BaseCRUD


class TempCRUD(BaseCRUD):
    async def create(self, entry: Temp):
        self.session.add(entry)
        await self.session.commit()

    async def get_temp(self, username: str) -> Temp:
        sql = text(f"select * from temp where username = '{username}'")
        res = await self.session.execute(sql)
        return res.scalar_one_or_none()
