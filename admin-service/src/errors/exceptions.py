class CustomError(ValueError):
    pass


class BudgetNotFound(CustomError):
    pass


class BudgetCreationFail(CustomError):
    pass
