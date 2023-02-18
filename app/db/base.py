# Import all the models, so that Base has them before being
# imported by Alembic

from app.api.temp.models import Temp
from app.api.users.models import UserModel
from app.api.domains.models import DomainModel
from app.db.base_model import Base
