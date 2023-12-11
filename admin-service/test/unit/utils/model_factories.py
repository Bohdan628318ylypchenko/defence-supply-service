from pydantic_factories import ModelFactory

from src.budget import models as budget_models
from src.availability import models as availability_models
from src.supply import models as supply_models


class BudgetFactory(ModelFactory):
    __model__ = budget_models.Budget


class CreateBudgetFactory(ModelFactory):
    __model__ = budget_models.CreateBudget


class AvailabilityFactory(ModelFactory):
    __model__ = availability_models.Availability


class AvailabilityIdFactory(ModelFactory):
    __model__ = availability_models.AvailabilityId


class CreateAvailabilityFactory(ModelFactory):
    __model__ = availability_models.CreateAvailability


class SupplyFactory(ModelFactory):
    __model__ = supply_models.Supply


class SupplyIdFactory(ModelFactory):
    __model__ = supply_models.SupplyId


class CreateSupplyFactory(ModelFactory):
    __model__ = supply_models.CreateSupply

