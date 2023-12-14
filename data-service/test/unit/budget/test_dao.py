import pytest 
from unittest.mock import AsyncMock
from src.budget.container import BudgetContainer
from src.budget.models import Budget, FullBudgetModel


@pytest.mark.asyncio
async def test_import_budget(
    budget_container: BudgetContainer,
    budget_model: Budget
) -> None:
    db_client_mock = AsyncMock()
    budget_container.db_client.override(db_client_mock)
    await budget_container.dao().import_budget(
        budget_list=[budget_model]
    )
    assert db_client_mock.import_budget.call_count == 1


@pytest.mark.asyncio
async def test_export_budget(
    budget_container: BudgetContainer,
    full_budget_model: FullBudgetModel,
    random_balance: float,
    random_year: int
) -> None:
    db_client_mock = AsyncMock()
    db_client_mock.export_budget.return_value = [full_budget_model]
    budget_container.db_client.override(db_client_mock)
    res = await budget_container.dao().export_budget(
        balance_min=random_balance,
        balance_max=random_balance,
        year_min=random_year,
        year_max=random_year
    )
    for i in res:
        assert isinstance(i, FullBudgetModel)
    assert res == [full_budget_model]
