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
