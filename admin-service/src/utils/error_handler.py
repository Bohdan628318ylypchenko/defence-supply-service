from typing import NoReturn
from src.errors import (
    http_exceptions,
    exceptions
)


def raise_exception(exception: exceptions.CustomError) -> NoReturn:
    api_errors = {
        exceptions.BudgetNotFound: http_exceptions.BUDGET_NOT_FOUND,
        exceptions.BudgetCreationFail: http_exceptions.BUDGET_CREATION_FAIL
    }
    raise api_errors.get(type(exception), http_exceptions.INTERNAL_ERROR) # type: ignore
