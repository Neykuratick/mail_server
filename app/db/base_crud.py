from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dep import get_session


class BaseCRUD:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session
