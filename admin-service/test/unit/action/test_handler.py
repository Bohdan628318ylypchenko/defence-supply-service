import pytest
from unittest.mock import AsyncMock
from src.action.container import ActionContainer
from src.action.models import ActionType, ExecutionStatus


@pytest.mark.parametrize("action_type", [action_type_name for action_type_name in ActionType])
@pytest.mark.asyncio
async def test_handle_action(
    action_container: ActionContainer,
    action_type: ActionType,
    user_id: int,
    action_description: str,
    action_type_id: int,
    action_id: int,
    execution_status: int
) -> None:
    mock = AsyncMock()
    mock.get_action_type_id.return_value = action_type_id
    mock.get_execution_status_id.return_value = execution_status
    mock.create_action.return_value = action_id
    action_container.dao.override(mock)
    res = await action_container.handler().handle_action(
        action_type=action_type,
        user_id=user_id,
        action_description=action_description
    )
    assert res == action_id



@pytest.mark.asyncio
async def test_create_availability_action(
    action_container: ActionContainer,
    action_id: int,
    entity_id: int,
    entity_action_id: int
) -> None:
    mock = AsyncMock()
    mock.create_availability_action.return_value = entity_action_id
    action_container.dao.override(mock)
    res = await action_container.handler().create_availability_action(
        action_id=action_id,
        availability_id=entity_id
    )
    assert res == entity_action_id


@pytest.mark.asyncio
async def test_create_supply_action(
    action_container: ActionContainer,
    action_id: int,
    entity_id: int,
    entity_action_id: int
) -> None:
    mock = AsyncMock()
    mock.create_budget_action.return_value = entity_action_id
    action_container.dao.override(mock)
    res = await action_container.handler().create_budget_action(
        action_id=action_id,
        budget_id=entity_id
    )
    assert res == entity_action_id


@pytest.mark.asyncio
async def test_create_budget_action(
    action_container: ActionContainer,
    action_id: int,
    entity_id: int,
    entity_action_id: int
) -> None:
    mock = AsyncMock()
    mock.create_supply_action.return_value = entity_action_id
    action_container.dao.override(mock)
    res = await action_container.handler().create_supply_action(
        action_id=action_id,
        supply_id=entity_id
    )
    assert res == entity_action_id


@pytest.mark.parametrize("entity_id", [None, 1])
@pytest.mark.asyncio
async def test_handle_execution_status(
    action_container: ActionContainer,
    action_id: int,
    entity_id: int,
    execution_status: int
)  -> None:
    mock = AsyncMock()
    mock.set_status.return_value = execution_status
    action_container.dao.override(mock)
    res = await action_container.handler().handle_execution_status(
        action_id=action_id,
        entity_id=entity_id
    )
    assert res == execution_status



