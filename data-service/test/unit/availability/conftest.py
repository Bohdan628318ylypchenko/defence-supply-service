from random import randint
import pytest
from datetime import date
from src.availability.container import AvailabilityContainer
from src.availability.models import Availability, FullAvailabilityModel
from test.unit.utils import model_factories


@pytest.fixture
def availability_container() -> AvailabilityContainer:
    return AvailabilityContainer()


@pytest.fixture
def availability_model() -> Availability:
    return model_factories.AvailabilityFactory.build()


@pytest.fixture
def full_availability_model() -> FullAvailabilityModel:
    return model_factories.FullAvailabilityModelFactory.build()


@pytest.fixture
def random_date() -> date:
    return date.today()


@pytest.fixture
def supply_id() -> int:
    return randint(1, 1000)
