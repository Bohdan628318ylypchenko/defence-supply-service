from unittest.mock import AsyncMock
import pytest
from src.budget.container import BudgetContainer
from src.budget.models import Budget, CreateBudget


@pytest.mark.asyncio
async def test_get_budget_by_id(
    budget_container: BudgetContainer,
    budget_model: Budget,
    action_id: int,
    budget_action_id: int,
    user_id: int,
    action_description: str
) -> None:
    dao_mock = AsyncMock()
    actions_mock = AsyncMock()
    actions_mock.handle_action.return_value = action_id
    actions_mock.create_budget_action.return_value = budget_action_id
    dao_mock.get_budget_by_id.return_value = budget_model
    budget_container.action_handler.override(actions_mock)
    budget_container.dao.override(dao_mock)
    res = await budget_container.handler().get_budget_by_id(
        user_id=user_id,
        action_description=action_description,
        budget_id=budget_model.id
    )
    assert res == budget_model
    assert actions_mock.handle_action.call_count == 1
    assert actions_mock.create_budget_action.call_count == 1
    assert actions_mock.handle_execution_status.call_count == 1



@pytest.mark.asyncio
async def test_get_budget_by_year(
    budget_container: BudgetContainer,
    budget_model: Budget,
    user_id: int,
    action_description: str
) -> None:
    dao_mock = AsyncMock()
    actions_mock = AsyncMock()
    dao_mock.get_budget_by_year.return_value = budget_model
    budget_container.action_handler.override(actions_mock)
    budget_container.dao.override(dao_mock)
    res = await budget_container.handler().get_budget_by_year(
        year=budget_model.year,
        user_id=user_id,
        action_description=action_description
    )
    assert res == budget_model
    assert actions_mock.handle_action.call_count == 1
    assert actions_mock.create_budget_action.call_count == 1
    assert actions_mock.handle_execution_status.call_count == 1


@pytest.mark.asyncio
async def test_create_budget(
    budget_container: BudgetContainer,
    budget_model: Budget,
    create_budget_model: CreateBudget,
    user_id: int,
    action_description: str
) -> None:
    actions_mock = AsyncMock()
    dao_mock = AsyncMock()
    dao_mock.create_budget.return_value = budget_model
    budget_container.action_handler.override(actions_mock)
    budget_container.dao.override(dao_mock)
    res = await budget_container.handler().create_budget(
        budget_body=create_budget_model,
        user_id=user_id,
        action_description=action_description
    )
    assert res == budget_model
    assert actions_mock.handle_action.call_count == 1
    assert actions_mock.create_budget_action.call_count == 1
    assert actions_mock.handle_execution_status.call_count == 1


@pytest.mark.asyncio
async def test_delete_budget_by_id(
    budget_container: BudgetContainer,
    budget_model: Budget,
    user_id: int,
    action_description: str
) -> None:
    actions_mock = AsyncMock()
    dao_mock = AsyncMock()
    dao_mock.delete_budget_by_id.return_value = budget_model
    budget_container.action_handler.override(actions_mock)
    budget_container.dao.override(dao_mock)
    res = await budget_container.handler().delete_budget_by_id(
        budget_id=budget_model.id,
        user_id=user_id,
        action_description=action_description
    )
    assert res == budget_model
    assert actions_mock.handle_action.call_count == 1
    assert actions_mock.create_budget_action.call_count == 1
    assert actions_mock.handle_execution_status.call_count == 1


@pytest.mark.asyncio
async def test_delete_budget_by_year(
    budget_container: BudgetContainer,
    budget_model: Budget,
    action_description: str,
    user_id: int
) -> None:
    actions_mock = AsyncMock()
    dao_mock = AsyncMock()
    dao_mock.delete_budget_by_year.return_value = budget_model
    budget_container.action_handler.override(actions_mock)
    budget_container.dao.override(dao_mock)
    res = await budget_container.handler().delete_budget_by_year(
        year=budget_model.year,
        user_id=user_id,
        action_description=action_description
    )
    assert res == budget_model
    assert actions_mock.handle_action.call_count == 1
    assert actions_mock.create_budget_action.call_count == 1
    assert actions_mock.handle_execution_status.call_count == 1
