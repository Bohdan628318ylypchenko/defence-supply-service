from unittest.mock import AsyncMock
import pytest
from src.availability.container import AvailabilityContainer
from src.availability.models import Availability, CreateAvailability


@pytest.mark.asyncio
async def test_get_availability_by_id(
    availability_container: AvailabilityContainer,
    availability_model: Availability
) -> None:
    mock = AsyncMock()
    mock.get_availability_by_id.return_value = availability_model.dict()
    availability_container.db_client.override(mock)
    res = await availability_container.dao().get_availability_by_id(
        availability_id=availability_model.id
    )
    assert res == availability_model


@pytest.mark.asyncio
async def test_get_availability_list_by_supply_id(
    availability_container: AvailabilityContainer,
    availability_model: Availability
) -> None:
    mock = AsyncMock()
    mock.get_availability_list_by_supply_id.return_value = [availability_model.dict()]
    availability_container.db_client.override(mock)
    res = await availability_container.dao().get_availability_list_by_supply_id(
        supply_id=availability_model.supply_id
    )
    assert res == [availability_model]


@pytest.mark.asyncio
async def test_create_availability(
    availability_container: AvailabilityContainer,
    availability_id_model: Availability,
    create_availability_model: CreateAvailability
) -> None:
    mock = AsyncMock()
    mock.create_availability.return_value = availability_id_model
    availability_container.db_client.override(mock)
    res = await availability_container.dao().create_availability(
        supply_id=create_availability_model.supply_id,
        unit_count=create_availability_model.unit_count,
        expiration_date=create_availability_model.expiration_date
    )
    assert res == availability_id_model


@pytest.mark.asyncio
async def test_delete_availability_by_id(
    availability_container: AvailabilityContainer,
    availability_model: Availability
) -> None:
    mock = AsyncMock()
    mock.delete_availability_by_id.return_value = availability_model.dict()
    availability_container.db_client.override(mock)
    res = await availability_container.dao().delete_availability_by_id(
        availability_id=availability_model.id
    )
    assert res == availability_model
