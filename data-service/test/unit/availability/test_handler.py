from datetime import date
from fastapi.exceptions import HTTPException
from fastapi.responses import StreamingResponse
import pytest
from unittest.mock import AsyncMock
from src.availability.container import AvailabilityContainer
from src.availability.models import FullAvailabilityModel
from .parametrize import (
    INVALID_HEADERS,
    INVALID_HEADERS_LEN,
    CSV_ROWS,
    INVALID_HEADERS_CSV_ROWS,
    INVALID_HEADERS_LEN_CSV_ROWS
)


@pytest.mark.asyncio
async def test_export_availability(
    availability_container: AvailabilityContainer,
    full_availability_model: FullAvailabilityModel,
    random_date: date,
    supply_id: int
) -> None:
    dao_mock = AsyncMock()
    dao_mock.export_availability.return_value = [full_availability_model]
    availability_container.dao.override(dao_mock)
    res = await availability_container.handler().export_availability(
        start_date=random_date,
        end_date=random_date,
        supply_id=supply_id
    )
    assert isinstance(res, StreamingResponse)


@pytest.mark.parametrize("contents", [CSV_ROWS, INVALID_HEADERS_CSV_ROWS, INVALID_HEADERS_LEN_CSV_ROWS])
@pytest.mark.asyncio 
async def test_import_availability(
    availability_container: AvailabilityContainer,
    contents: list[str]
) -> None:
    dao_mock = AsyncMock()
    availability_container.dao.override(dao_mock)
    if INVALID_HEADERS_LEN in contents or INVALID_HEADERS in contents:
        with pytest.raises(HTTPException):
            await availability_container.handler().import_availability(
                contents=contents
            )
    else:
        await availability_container.handler().import_availability(
            contents=contents
        )
        assert dao_mock.import_availability.call_count == 1
