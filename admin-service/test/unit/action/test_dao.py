import pytest
from unittest.mock import AsyncMock
from src.action.container import ActionContainer
from src.action.models import ActionType, ExecutionStatus


@pytest.mark.asyncio
async def test_create_action(
    action_container: ActionContainer,
    user_id: int,
    action_description: str,
    action_type_id: int,
    execution_status: int,
    action_id: int
) -> None:
    mock = AsyncMock()
    mock.create_action.return_value = action_id
    action_container.db_client.override(mock)
    res = await action_container.dao().create_action(
        user_id=user_id,
        action_description=action_description,
        action_type_id=action_type_id,
        execution_status=execution_status
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
    action_container.db_client.override(mock)
    res = await action_container.dao().create_availability_action(
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
    action_container.db_client.override(mock)
    res = await action_container.dao().create_budget_action(
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
    action_container.db_client.override(mock)
    res = await action_container.dao().create_supply_action(
        action_id=action_id,
        supply_id=entity_id
    )
    assert res == entity_action_id


@pytest.mark.asyncio
async def test_set_status(
    action_container: ActionContainer,
    action_id: int,
    execution_status: int
) -> None:
    mock = AsyncMock()
    action_container.db_client.override(mock)
    await action_container.dao().set_status(
        action_id=action_id,
        execution_status_id=execution_status
    )
    assert mock.set_status.call_count == 1


@pytest.mark.parametrize("execution_status_name", [execution_status for execution_status in ExecutionStatus])
@pytest.mark.asyncio
async def test_get_execution_status_id(
    action_container: ActionContainer,
    execution_status: int,
    execution_status_name: ExecutionStatus
) -> None:
    mock = AsyncMock()
    mock.get_execution_status_id.return_value = execution_status
    action_container.db_client.override(mock)
    res = await action_container.dao().get_execution_status_id(
        execution_status=execution_status_name
    )
    assert res == execution_status
    assert mock.get_execution_status_id.call_count == 1


@pytest.mark.parametrize("action_type_name", [action_type for action_type in ActionType])
@pytest.mark.asyncio
async def test_get_action_type_id(
    action_container: ActionContainer,
    action_type_id: int,
    action_type_name: ActionType
) -> None:
    mock = AsyncMock()
    mock.get_action_type_id.return_value = action_type_id
    action_container.db_client.override(mock)
    res = await action_container.dao().get_action_type_id(
        action_type=action_type_name
    )
    assert res == action_type_id
    assert mock.get_action_type_id.call_count == 1
