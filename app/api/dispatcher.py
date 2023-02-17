from fastapi import APIRouter
from app.api.users.handlers import router as users_router
from app.api.security.handlers import router as security_router
from app.core.config import settings

api_router = APIRouter(prefix=settings.API_V1_URL)
api_router.include_router(users_router, tags=["users"])
api_router.include_router(security_router, tags=["security"])
