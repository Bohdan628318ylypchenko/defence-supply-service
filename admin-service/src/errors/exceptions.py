class CustomError(ValueError):
    pass


class BudgetNotFound(CustomError):
    pass


class BudgetCreationFail(CustomError):
    pass


class SupplyNotFound(CustomError):
    pass


class SupplyCreationFail(CustomError):
    pass


class ActionCreationFail(CustomError):
    pass


class AvailabilityNotFound(CustomError):
    pass


class AvailabilityCreationFail(CustomError):
    pass


class CreateBudgetActionFail(CustomError):
    pass


class CreateSupplyActionFail(CustomError):
    pass


class CreateAvailabilityActionFail(CustomError):
    pass


class ExecutionStatusNotFound(CustomError):
    pass 


class ActionTypeNotFound(CustomError):
    pass


class StatusUpdateError(CustomError):
    pass
