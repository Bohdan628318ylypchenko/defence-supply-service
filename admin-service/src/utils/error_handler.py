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
        exceptions.AvailabilityCreationFail: http_exceptions.AVAILABILITY_CREATION_FAIL
    }
    raise api_errors.get(type(exception), http_exceptions.INTERNAL_ERROR) # type: ignore
