from fastapi import APIRouter

from app.api.permissions.admin import PermissionActionsAdmin
from app.api.permissions.admin import PermissionTargetsActionsAdmin
from app.api.permissions.admin import PermissionTargetsAdmin
from app.api.roles.admin import RolesAdmin
from app.api.roles.admin import RolesTargetActionsAdmin
from app.core.config import settings
from app.api.domains.admin import DomainAdmin
from app.api.users.admin import UserAdmin
from app.api.users.handlers import router as users_router
from app.api.security.handlers import router as security_router
from app.api.domains.handlers import router as domains_router

api_router = APIRouter(prefix=settings.API_V1_URL)
api_router.include_router(users_router, tags=["users"])
api_router.include_router(security_router, tags=["security"])
api_router.include_router(domains_router, tags=["domains"])


admin_views = [
    UserAdmin,
    DomainAdmin,
    PermissionTargetsAdmin,
    PermissionActionsAdmin,
    PermissionTargetsActionsAdmin,
    RolesAdmin,
    RolesTargetActionsAdmin,
]
