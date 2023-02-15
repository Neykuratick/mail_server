# Import all the models, so that Base has them before being
# imported by Alembic

from app.database.base_model import Base  # noqa
from app.temp.models import Temp  # noqa
from app.users.models import User  # noqa