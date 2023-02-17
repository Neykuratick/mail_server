# Import all the models, so that Base has them before being
# imported by Alembic

from app.db.base_model import Base  # noqa
from app.api.temp.models import Temp  # noqa
from app.api.users.models import User  # noqa
