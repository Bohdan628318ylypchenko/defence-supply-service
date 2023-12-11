from unittest.mock import AsyncMock
import pytest
from src.availability.container import AvailabilityContainer
from src.availability.models import Availability, AvailabilityId, CreateAvailability 


@pytest.mark.asyncio
async def test_get_availability_by_id(
    availability_container: AvailabilityContainer,
    availability_model: Availability,
    action_id: int,
    user_id: int,
    action_description: str,
    availability_action_id: int
) -> None:
    dao_mock = AsyncMock()
    actions_mock = AsyncMock()
    actions_mock.handle_action.return_value = action_id
    actions_mock.create_availability_action.return_value = availability_action_id
    dao_mock.get_availability_by_id.return_value = availability_model
    availability_container.action_handler.override(actions_mock)
    availability_container.dao.override(dao_mock)
    res = await availability_container.handler().get_availability_by_id(
        user_id=user_id,
        action_description=action_description,
        availability_id=availability_model.id
    )
    assert res == availability_model
    assert actions_mock.handle_action.call_count == 1
    assert actions_mock.create_availability_action.call_count == 1
    assert actions_mock.handle_execution_status.call_count == 1



@pytest.mark.asyncio
async def test_get_availability_list_by_supply_id(
    availability_container: AvailabilityContainer,
    availability_model: Availability,
    action_id: int,
    user_id: int,
    action_description: str,
    availability_action_id: int
) -> None:
    dao_mock = AsyncMock()
    actions_mock = AsyncMock()
    actions_mock.handle_action.return_value = action_id
    actions_mock.create_availability_action.return_value = availability_action_id
    dao_mock.get_availability_list_by_supply_id.return_value = [availability_model]
    availability_container.action_handler.override(actions_mock)
    availability_container.dao.override(dao_mock)
    res = await availability_container.handler().get_availability_list_by_supply_id(
        user_id=user_id,
        action_description=action_description,
        supply_id=availability_model.supply_id
    )
    assert res == [availability_model]
    assert actions_mock.handle_action.call_count == 1
    assert actions_mock.create_availability_action.call_count == 1
    assert actions_mock.handle_execution_status.call_count == 1


@pytest.mark.asyncio
async def test_delete_availability_by_id(
    availability_container: AvailabilityContainer,
    availability_model: Availability,
    action_id: int,
    user_id: int,
    action_description: str,
    availability_action_id: int
) -> None:
    dao_mock = AsyncMock()
    actions_mock = AsyncMock()
    actions_mock.handle_action.return_value = action_id
    actions_mock.create_availability_action.return_value = availability_action_id
    dao_mock.delete_availability_by_id.return_value = availability_model
    availability_container.action_handler.override(actions_mock)
    availability_container.dao.override(dao_mock)
    res = await availability_container.handler().delete_availability_by_id(
        user_id=user_id,
        action_description=action_description,
        availability_id=availability_model.id
    )
    assert res == availability_model
    assert actions_mock.handle_action.call_count == 1
    assert actions_mock.create_availability_action.call_count == 1
    assert actions_mock.handle_execution_status.call_count == 1


@pytest.mark.asyncio
async def test_create_availability(
    availability_container: AvailabilityContainer,
    create_availability_model: CreateAvailability,
    availability_id_model: AvailabilityId,
    action_id: int,
    user_id: int,
    action_description: str,
    availability_action_id: int
) -> None:
    dao_mock = AsyncMock()
    actions_mock = AsyncMock()
    actions_mock.handle_action.return_value = action_id
    actions_mock.create_availability_action.return_value = availability_action_id
    dao_mock.create_availability.return_value = availability_id_model
    availability_container.action_handler.override(actions_mock)
    availability_container.dao.override(dao_mock)
    res = await availability_container.handler().create_availability(
        user_id=user_id,
        action_description=action_description,
        availability_body=create_availability_model
    )
    assert res == availability_id_model
    assert actions_mock.handle_action.call_count == 1
    assert actions_mock.create_availability_action.call_count == 1
    assert actions_mock.handle_execution_status.call_count == 1
