from typing import NoReturn
from src.errors import (
    http_exceptions,
    exceptions
)


def raise_exception(exception: exceptions.CustomError) -> NoReturn:
    api_errors = {
        exceptions.BudgetNotFound: http_exceptions.BUDGET_NOT_FOUND,
        exceptions.BudgetCreationFail: http_exceptions.BUDGET_CREATION_FAIL,
        exceptions.SupplyNotFound: http_exceptions.SUPPLY_NOT_FOUND,
        exceptions.SupplyCreationFail: http_exceptions.SUPPLY_CREATION_FAIL,
        exceptions.ActionCreationFail: http_exceptions.ACTION_CREATION_FAIL,
        exceptions.AvailabilityNotFound: http_exceptions.AVAILABILITY_NOT_FOUND,
        exceptions.AvailabilityCreationFail: http_exceptions.AVAILABILITY_CREATION_FAIL,
        exceptions.CreateSupplyActionFail: http_exceptions.SUPPLY_ACTION_CREATION_FAIL,
        exceptions.CreateBudgetActionFail: http_exceptions.BUDGET_ACTION_CREATION_FAIL,
        exceptions.CreateAvailabilityActionFail: http_exceptions.AVAILABILITY_ACTION_CREATION_FAIL,
        exceptions.ExecutionStatusNotFound: http_exceptions.EXECUTION_STATUS_NOT_FOUND,
        exceptions.ActionTypeNotFound: http_exceptions.ACTION_TYPE_NOT_FOUND,
        exceptions.StatusUpdateError: http_exceptions.STATUS_UPDATE_FAIL,
        exceptions.SupplyNameUniqueViolation: http_exceptions.SUPPLY_NAME_UNIQUE_VIOLATION,
        exceptions.BudgetYearUniqueViolation: http_exceptions.BUDGET_YEAR_UNIQUE_VIOLATION
    }
    raise api_errors.get(type(exception), http_exceptions.INTERNAL_ERROR) # type: ignore
