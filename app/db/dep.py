from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_async_engine(settings.POSTGRES_URL_ASYNC, echo=False)
async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
