from enum import Enum
from enum import auto


# WARNING!! EVERY MODIFICATION OF THIS ENUM REQUIRES A MIGRATION
# see https://stackoverflow.com/a/65173731/13246657
# tldr see migration 2023_02_26_1637-5a077a981eb0_add_enums


class TargetsEnum(str, Enum):
    DOMAIN = auto()
    USER = auto()
    PERMISSION = auto()
    TARGET = auto()
    ROLE = auto()


class ActionsEnm(str, Enum):
    CREATE = auto()
    READ = auto()
    UPDATE = auto()
    DELETE = auto()
