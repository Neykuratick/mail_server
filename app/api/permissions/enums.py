from enum import Enum
from enum import auto


# When adding new Target or Action, you must write a migration to add it to db


class TargetsEnum(str, Enum):
    def _generate_next_value_(self, start, count, last_values):
        return self.upper()

    DOMAIN = auto()
    USER = auto()
    PERMISSION = auto()
    TARGET = auto()
    ROLE = auto()


class ActionsEnum(str, Enum):
    def _generate_next_value_(self, start, count, last_values):
        return self.upper()

    CREATE = auto()
    READ = auto()
    UPDATE = auto()
    DELETE = auto()
