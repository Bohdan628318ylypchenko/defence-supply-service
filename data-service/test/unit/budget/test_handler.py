from fastapi.responses import StreamingResponse
import pytest 
from unittest.mock import AsyncMock
from src.budget.container import BudgetContainer
from src.budget.models import Budget, FullBudgetModel
from fastapi.exceptions import HTTPException
from test.unit.budget.parametrize import (
    csv_rows,
    invalid_csv_rows,
    invalid_headers, 
    invalid_len_header,
    invalid_len_csv_rows
)


@pytest.mark.parametrize("contents", [csv_rows, invalid_csv_rows, invalid_len_csv_rows])
@pytest.mark.asyncio
async def test_import_budget(
    budget_container: BudgetContainer,
    contents: list[str]
) -> None:
    dao_mock = AsyncMock()
    budget_container.dao.override(dao_mock)
    if invalid_headers in contents or invalid_len_header in contents:
        with pytest.raises(HTTPException):
            await budget_container.handler().import_budget(
                contents=contents
            )
    else:
        await budget_container.handler().import_budget(
            contents=contents
        )
        assert dao_mock.import_budget.call_count == 1


@pytest.mark.asyncio
async def test_export_budget(
    budget_container: BudgetContainer,
    full_budget_model: FullBudgetModel,
    random_balance: float,
    random_year: int
) -> None:
    dao_mock = AsyncMock()
    dao_mock.export_budget.return_value = [full_budget_model]
    budget_container.dao.override(dao_mock)
    res = await budget_container.handler().export_budget(
        balance_min=random_balance,
        balance_max=random_balance,
        year_min=random_year,
        year_max=random_year
    )
    assert isinstance(res, StreamingResponse)
