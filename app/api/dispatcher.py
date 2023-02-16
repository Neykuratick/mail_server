from fastapi import APIRouter
from app.api.users.handlers import router as users_router

api_router = APIRouter(prefix='/api')
api_router.include_router(users_router, tags=["users"], prefix='/users')
