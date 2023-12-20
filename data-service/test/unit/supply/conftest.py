import pytest
from random import random, randint
from src.supply.models import FullSupplyModel, Supply
from test.unit.utils import model_factories
from src.supply.container import SupplyContainer


@pytest.fixture
def supply_container() -> SupplyContainer:
    return SupplyContainer()


@pytest.fixture
def supply_model() -> Supply:
    return model_factories.SupplyFactory.build()


@pytest.fixture
def full_supply_model() -> FullSupplyModel:
    return  model_factories.FullSupplyModelFactory.build()


@pytest.fixture
def unit_cost() -> float:
    return random()


@pytest.fixture
def norm_unit_count_day() -> float:
    return random()


@pytest.fixture
def unit_type() -> str:
    return "someunit"
