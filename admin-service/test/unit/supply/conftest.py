from unittest.mock import AsyncMock
import pytest
from src.supply.container import SupplyContainer
from src.supply.models import CreateSupply, Supply, SupplyId
from test.unit.utils import model_factories

class AsyncMagicMock(AsyncMock):

    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc, tb): 
        pass


@pytest.fixture
def supply_container() -> SupplyContainer:
    return SupplyContainer()


@pytest.fixture() 
def supply_model() -> Supply:
    return model_factories.SupplyFactory.build()
    

@pytest.fixture
def supply_id_model(
    supply_model: Supply
) -> SupplyId:
    return model_factories.SupplyIdFactory.build(
        id=supply_model.id
    )


@pytest.fixture
def create_supply_model(
    supply_model: Supply
) -> CreateSupply:
    return model_factories.CreateSupplyFactory.build(
        name=supply_model.name,
        unit_cost=supply_model.unit_cost,
        unit_type=supply_model.unit_type,
        norm_unit_count_day=supply_model.norm_unit_count_day
    )


@pytest.fixture
def async_magic_mock() -> AsyncMagicMock:
    return AsyncMagicMock()
