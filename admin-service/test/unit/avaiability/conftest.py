import random
import pytest
from src.availability.container import AvailabilityContainer
from src.availability.models import Availability, AvailabilityId, CreateAvailability
from test.unit.utils import model_factories


@pytest.fixture
def availability_container() -> AvailabilityContainer:
    return AvailabilityContainer()


@pytest.fixture
def availability_model() -> Availability:
    return model_factories.AvailabilityFactory.build()


@pytest.fixture
def availability_id_model(
    availability_model: Availability
) -> AvailabilityId:
    return model_factories.AvailabilityIdFactory.build(id=availability_model.id)


@pytest.fixture
def create_availability_model(
    availability_model: Availability
) -> CreateAvailability:
    return model_factories.CreateAvailabilityFactory.build(
        supply_id=availability_model.supply_id,
        unit_count=availability_model.unit_count,
        expiration_date=availability_model.expiration_date
    )


@pytest.fixture
def availability_action_id() -> int:
    return random.randint(1, 100)
