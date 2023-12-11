class CustomError(ValueError):
    pass


class InvalidBudgetImportHeader(CustomError):
    pass


class InvalidBudgetImportBody(CustomError):
    pass


class BudgetYearUniqueViolation(CustomError):
    pass


class SupplyUniqueViolationError(CustomError):
    pass


class InvalidSupplyImportHeader(CustomError):
    pass


class InvalidSupplyImportBody(CustomError):
    pass


class AvailabilityForeignKeyViolation(CustomError):
    pass


class InvalidAvailabilityImportHeader(CustomError):
    pass


class InvalidAvailabilityImportBody(CustomError):
    pass
