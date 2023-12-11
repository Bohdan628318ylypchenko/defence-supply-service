from typing import NoReturn
from src.errors import (
    http_exceptions,
    exceptions
)


def raise_exception(exception: exceptions.CustomError) -> NoReturn:
    api_errors = {
        exceptions.InvalidBudgetImportHeader: http_exceptions.INVALID_BUDGET_IMPORT_HEADER_ERROR,
        exceptions.InvalidBudgetImportBody: http_exceptions.INVALID_BUDGET_IMPORT_BODY_ERROR,
        exceptions.BudgetYearUniqueViolation: http_exceptions.BUDGET_YEAR_UNIQUE_VIOLATION,
        exceptions.SupplyUniqueViolationError: http_exceptions.SUPPLY_UNIQUE_VIOLATION_ERROR,
        exceptions.InvalidSupplyImportHeader: http_exceptions.INVALID_SUPPLY_IMPORT_HEADER_ERROR,
        exceptions.InvalidSupplyImportBody: http_exceptions.INVALID_SUPPLY_IMPORT_BODY_ERROR,
        exceptions.AvailabilityForeignKeyViolation: http_exceptions.AVAILABILITY_FOREIGN_KEY_VIOLATION,
        exceptions.InvalidAvailabilityImportBody: http_exceptions.INVALID_AVAILABILITY_IMPORT_BODY,
        exceptions.InvalidAvailabilityImportHeader: http_exceptions.INVALID_AVAILABILITY_IMPORT_HEADER
    }
    raise api_errors.get(type(exception), http_exceptions.INTERNAL_ERROR) # type: ignore
