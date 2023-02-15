from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.dep import get_session

app = FastAPI()


@app.get("/")
async def read_root(db: AsyncSession = Depends(get_session)):
    return {"message": "hello, world"}
