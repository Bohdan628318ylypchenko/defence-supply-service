from fastapi.responses import StreamingResponse
from fastapi.exceptions import HTTPException
import pytest
from unittest.mock import AsyncMock
from src.supply.container import SupplyContainer
from src.supply.models import FullSupplyModel, Supply
from .parametrize import (
    INVALID_HEADERS,
    INVALID_LEN_HEADERS,
    CSV_ROWS,
    INVALID_HEADERS_CSV_ROW,
    INVALID_LEN_HEADERS_CSV_ROW
)


@pytest.mark.asyncio 
async def test_export_supply(
    supply_container: SupplyContainer,
    norm_unit_count_day: float,
    unit_cost: float,
    unit_type: str,
    full_supply_model: FullSupplyModel
) -> None:
    dao_mock = AsyncMock()
    dao_mock.export_supply.return_value = [full_supply_model]
    supply_container.dao.override(dao_mock)
    res = await supply_container.handler().export_supply(
        unit_cost_min=unit_cost,
        unit_cost_max=unit_cost,
        unit_type=unit_type,
        norm_unit_count_day_min=norm_unit_count_day,
        norm_unit_count_day_max=norm_unit_count_day
    )
    assert isinstance(res, StreamingResponse)


@pytest.mark.parametrize("contents", [CSV_ROWS, INVALID_HEADERS_CSV_ROW, INVALID_LEN_HEADERS_CSV_ROW])
@pytest.mark.asyncio
async def test_import_supply(
    supply_container: SupplyContainer,
    contents: list[str]
) -> None:
    dao_mock = AsyncMock()
    supply_container.dao.override(dao_mock)
    if INVALID_HEADERS in contents or INVALID_LEN_HEADERS in contents:
        with pytest.raises(HTTPException):
            await supply_container.handler().import_supply(
                contents=contents
            )
    else:
        await supply_container.handler().import_supply(
            contents=contents
        )
        assert dao_mock.import_supply.call_count == 1
