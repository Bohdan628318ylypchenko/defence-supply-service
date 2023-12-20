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
    database_mock = AsyncMock()
    availability_container.database.override(database_mock)
    await availability_container.db_client().import_availability(
        availability_list=[availability_model]
    )
    assert database_mock.execute_many.call_count == 1


@pytest.mark.asyncio
async def test_export_availability(
    availability_container: AvailabilityContainer,
    full_availability_model: FullAvailabilityModel,
    random_date: date,
    supply_id: int
) -> None:
    database_mock = AsyncMock()
    database_mock.fetch_all.return_value = [full_availability_model.dict()]
    availability_container.database.override(database_mock)
    res = await availability_container.db_client().export_availability(
        start_date=random_date,
        end_date=random_date,
        supply_id=supply_id
    )
    assert database_mock.fetch_all.call_count == 1
    assert res == [full_availability_model]
