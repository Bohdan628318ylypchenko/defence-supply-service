from asyncio import Future
import pytest
from unittest.mock import AsyncMock, Mock
from src.supply.container import SupplyContainer
from src.supply.models import CreateSupply, Supply, SupplyId


@pytest.mark.asyncio
async def test_get_supply_by_id(
    supply_container: SupplyContainer,
    supply_model: Supply
) -> None:
    mock = AsyncMock()
    mock.fetch_one.return_value = supply_model.dict()
    supply_container.database.override(mock)
    res = await supply_container.db_client().get_supply_by_id(
        supply_id=supply_model.id
    )
    assert res == supply_model


@pytest.mark.asyncio
async def test_get_supply_by_name(
    supply_container: SupplyContainer,
    supply_model: Supply
) -> None:
    mock = AsyncMock()
    mock.fetch_one.return_value = supply_model.dict()
    supply_container.database.override(mock)
    res = await supply_container.db_client().get_supply_by_name(
        name=supply_model.name
    )
    assert res == supply_model


@pytest.mark.asyncio
async def test_delete_supply_by_id(
    supply_model: Supply,
    supply_container: SupplyContainer,
    async_magic_mock
) -> None:
    mock = Mock()
    mock.transaction.return_value = async_magic_mock
    supply_model_future = Future()
    supply_model_future.set_result(supply_model.dict())
    execute_future = Future()
    execute_future.set_result(None)
    mock.fetch_one.return_value = supply_model_future
    mock.execute.return_value = execute_future
    supply_container.database.override(mock)
    res = await supply_container.db_client().delete_supply_by_id(
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
    mock.execute.return_value = supply_id_model.id
    supply_container.database.override(mock)
    res = await supply_container.db_client().create_supply(
        name=create_supply_model.name,
        unit_cost=create_supply_model.unit_cost,
        unit_type=create_supply_model.unit_type,
        norm_unit_count_day=create_supply_model.norm_unit_count_day
    )
    assert res == supply_id_model

