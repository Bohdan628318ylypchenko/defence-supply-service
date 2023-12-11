import pytest
from unittest.mock import AsyncMock
from src.supply.container import SupplyContainer
from src.supply.models import CreateSupply, Supply, SupplyId


@pytest.mark.asyncio
async def test_get_supply_by_id(
    supply_container: SupplyContainer,
    supply_model: Supply
) -> None:
    mock = AsyncMock()
    mock.get_supply_by_id.return_value = supply_model
    supply_container.db_client.override(mock)
    res = await supply_container.dao().get_supply_by_id(
        supply_id=supply_model.id
    )
    assert res == supply_model


@pytest.mark.asyncio
async def test_get_supply_by_name(
    supply_container: SupplyContainer,
    supply_model: Supply
) -> None:
    mock = AsyncMock()
    mock.get_supply_by_name.return_value = supply_model
    supply_container.db_client.override(mock)
    res = await supply_container.dao().get_supply_by_name(
        name=supply_model.name
    )
    assert res == supply_model


@pytest.mark.asyncio
async def test_delete_supply_by_id(
    supply_model: Supply,
    supply_container: SupplyContainer,
) -> None:
    mock = AsyncMock()
    mock.delete_supply_by_id.return_value = supply_model
    supply_container.db_client.override(mock)
    res = await supply_container.dao().delete_supply_by_id(
        supply_id=supply_model.id
    )
    assert res == supply_model


@pytest.mark.asyncio
async def test_create_supply(
    create_supply_model: CreateSupply,
    supply_container: SupplyContainer,
    supply_id_model: SupplyId
) -> None:
    mock = AsyncMock()
    mock.create_supply.return_value = supply_id_model
    supply_container.db_client.override(mock)
    res = await supply_container.dao().create_supply(
        name=create_supply_model.name,
        unit_cost=create_supply_model.unit_cost,
        unit_type=create_supply_model.unit_type,
        norm_unit_count_day=create_supply_model.norm_unit_count_day
    )
    assert res == supply_id_model
