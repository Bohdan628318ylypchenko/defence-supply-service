from unittest.mock import AsyncMock
from src.supply.container import SupplyContainer
from src.supply.models import FullSupplyModel, Supply
import pytest


@pytest.mark.asyncio
async def test_import_supply(
    supply_container: SupplyContainer,
    supply_model: Supply
) -> None:
    db_client_mock = AsyncMock()
    supply_container.db_client.override(db_client_mock)
    await supply_container.dao().import_supply(
        supply_list=[supply_model]
    )
    assert db_client_mock.import_supply.call_count == 1


@pytest.mark.asyncio
async def test_export_supply(
    unit_cost: float,
    norm_unit_count_day: float,
    unit_type: str,
    full_supply_model: FullSupplyModel,
    supply_container: SupplyContainer
) -> None:
    db_client_mock = AsyncMock()
    db_client_mock.export_supply.return_value = [full_supply_model]
    supply_container.db_client.override(db_client_mock)
    res = await supply_container.dao().export_supply(
        norm_unit_count_day_min=norm_unit_count_day,
        norm_unit_count_day_max=norm_unit_count_day,
        unit_type=unit_type,
        unit_cost_min=unit_cost,
        unit_cost_max=unit_cost
    )
    assert res == [full_supply_model]
    assert db_client_mock.export_supply.call_count == 1

