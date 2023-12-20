from datetime import date
from unittest.mock import AsyncMock
import pytest
from src.availability.container import AvailabilityContainer
from src.availability.models import Availability, FullAvailabilityModel


@pytest.mark.asyncio
async def test_import_availability(
    availability_container: AvailabilityContainer,
    availability_model: Availability
) -> None:
    db_client_mock = AsyncMock()
    availability_container.db_client.override(db_client_mock)
    await availability_container.dao().import_availability(
        availability_list=[availability_model]
    )
    assert db_client_mock.import_availability.call_count == 1


@pytest.mark.asyncio
async def test_export_availability(
    availability_container: AvailabilityContainer,
    full_availability_model: FullAvailabilityModel,
    random_date: date,
    supply_id: int
) -> None:
    db_client_mock = AsyncMock()
    db_client_mock.export_availability.return_value = [full_availability_model]
    availability_container.db_client.override(db_client_mock)
    res = await availability_container.dao().export_availability(
        start_date=random_date,
        end_date=random_date,
        supply_id=supply_id
    )
    assert db_client_mock.export_availability.call_count == 1
    assert res == [full_availability_model]
