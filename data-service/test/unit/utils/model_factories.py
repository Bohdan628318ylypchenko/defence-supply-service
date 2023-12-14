from pydantic_factories import ModelFactory
from src.availability import models as availability_models
from src.budget import models as budget_models
from src.supply import models as supply_models


class BudgetFactory(ModelFactory):
    __model__ = budget_models.Budget


class FullBudgetModelFactory(ModelFactory):
    __model__ = budget_models.FullBudgetModel


class SupplyFactory(ModelFactory):
    __model__ = supply_models.Supply


class FullSupplyModelFactory(ModelFactory):
    __model__ = supply_models.FullSupplyModel


class AvailabilityFactory(ModelFactory):
    __model__ = availability_models.Availability


class FullAvailabilityModelFactory(ModelFactory):
    __model__ = availability_models.FullAvailabilityModel
