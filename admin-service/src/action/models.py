from enum import Enum


class ActionType(str, Enum):
    CREATE = "create"
    GET = "get"
    DELETE = "delete"


class EntityAction(str, Enum):
    SUPPLY_ACTION = "supply_action"
    AVAILABILITY_ACTION = "availability_action"
    BUDGET_ACTION = "budget_action"


class ExecutionStatus(str, Enum):
    SUCCESS = "success"
    FAIL = "fail"

