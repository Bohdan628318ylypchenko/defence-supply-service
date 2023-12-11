from unittest.mock import AsyncMock
import pytest
from src.budget.container import BudgetContainer
from src.budget.models import Budget


@pytest.mark.asyncio
async def test_get_budget_by_id(
    budget_container: BudgetContainer,
    budget_model: Budget
) -> None:
    mock = AsyncMock()
    mock.get_budget_by_id.return_value = budget_model
    budget_container.db_client.override(mock)
    res = await budget_container.dao().get_budget_by_id(
        budget_id=budget_model.id
    )
    assert res == budget_model


@pytest.mark.asyncio
async def test_get_budget_by_year(
    budget_container: BudgetContainer,
    budget_model: Budget
) -> None:
    mock = AsyncMock()
    mock.get_budget_by_year.return_value = budget_model.dict()
    budget_container.db_client.override(mock)
    res = await budget_container.dao().get_budget_by_year(
        year=budget_model.year
    )
    assert res == budget_model


@pytest.mark.asyncio
async def test_create_budget(
    budget_container: BudgetContainer,
    budget_model: Budget
) -> None:
    mock = AsyncMock()
    mock.create_budget.return_value = budget_model.dict()
    budget_container.db_client.override(mock)
    res = await budget_container.dao().create_budget(
        year=budget_model.year,
        balance=budget_model.balance
    )
    assert res == budget_model


@pytest.mark.asyncio
async def test_delete_budget_by_id(
    budget_container: BudgetContainer,
    budget_model: Budget
) -> None:
    mock = AsyncMock()
    mock.delete_budget_by_id.return_value = budget_model.dict()
    budget_container.db_client.override(mock)
    res = await budget_container.dao().delete_budget_by_id(
        budget_id=budget_model.id
    )
    assert res == budget_model


@pytest.mark.asyncio
async def test_delete_budget_by_year(
    budget_container: BudgetContainer,
    budget_model: Budget
) -> None:
    mock = AsyncMock()
    mock.delete_budget_by_year.return_value = budget_model.dict()
    budget_container.db_client.override(mock)
    res = await budget_container.dao().delete_budget_by_year(
        year=budget_model.year
    )
    assert res == budget_model

