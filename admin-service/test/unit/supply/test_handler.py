import pytest
from unittest.mock import AsyncMock

from src.supply.container import SupplyContainer
from src.supply.models import CreateSupply, Supply, SupplyId


@pytest.mark.asyncio
async def test_get_supply_by_id(
    supply_container: SupplyContainer,
    supply_model: Supply,
    user_id: int,
    action_description: str
) -> None:
    mock = AsyncMock()
    actions_mock = AsyncMock()
    mock.get_supply_by_id.return_value = supply_model
    supply_container.action_handler.override(actions_mock)
    supply_container.dao.override(mock)
    res = await supply_container.handler().get_supply_by_id(
        supply_id=supply_model.id,
        user_id=user_id,
        action_description=action_description
    )
    assert actions_mock.handle_action.call_count == 1
    assert actions_mock.create_supply_action.call_count == 1
    assert actions_mock.handle_execution_status.call_count == 1
    assert res == supply_model


@pytest.mark.asyncio
async def test_get_supply_by_name(
    supply_container: SupplyContainer,
    supply_model: Supply,
    user_id: int,
    action_description: str
) -> None:
    mock = AsyncMock()
    actions_mock = AsyncMock()
    mock.get_supply_by_name.return_value = supply_model
    supply_container.action_handler.override(actions_mock)
    supply_container.dao.override(mock)
    res = await supply_container.handler().get_supply_by_name(
        name=supply_model.name,
        user_id=user_id,
        action_description=action_description
    )
    assert actions_mock.handle_action.call_count == 1
    assert actions_mock.create_supply_action.call_count == 1
    assert actions_mock.handle_execution_status.call_count == 1
    assert res == supply_model


@pytest.mark.asyncio
async def test_delete_supply_by_id(
    supply_model: Supply,
    supply_container: SupplyContainer,
    user_id: int,
    action_description: str
) -> None:
    mock = AsyncMock()
    actions_mock = AsyncMock()
    mock.delete_supply_by_id.return_value = supply_model
    supply_container.action_handler.override(actions_mock)
    supply_container.dao.override(mock)
    res = await supply_container.handler().delete_supply_by_id(
        supply_id=supply_model.id,
        user_id=user_id,
        action_description=action_description
    )
    assert actions_mock.handle_action.call_count == 1
    assert actions_mock.create_supply_action.call_count == 1
    assert actions_mock.handle_execution_status.call_count == 1
    assert res == supply_model


@pytest.mark.asyncio
async def test_create_supply(
    create_supply_model: CreateSupply,
    supply_container: SupplyContainer,
    supply_id_model: SupplyId,
    user_id: int,
    action_description: str
) -> None:
    mock = AsyncMock()
    actions_mock = AsyncMock()
    mock.create_supply.return_value = supply_id_model
    supply_container.action_handler.override(actions_mock)
    supply_container.dao.override(mock)
    res = await supply_container.handler().create_supply(
        supply_body=create_supply_model,
        user_id=user_id,
        action_description=action_description
    )
    assert res == supply_id_model
    assert actions_mock.handle_action.call_count == 1
    assert actions_mock.create_supply_action.call_count == 1
    assert actions_mock.handle_execution_status.call_count == 1
