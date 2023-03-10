# Import all the models, so that Base has them before being
# imported by Alembic

from app.api.temp.models import Temp  # noqa
from app.api.users.models import UserModel  # noqa
from app.api.domains.models import DomainModel  # noqa
from app.api.permissions.models import PermissionTargetModel  # noqa
from app.api.permissions.models import PermissionActionModel  # noqa
from app.api.permissions.models import PermissionTargetsActions  # noqa
from app.api.roles.models import RoleModel  # noqa
from app.api.roles.models import RolesTargetActions  # noqa
from app.db.base_model import Base  # noqa
