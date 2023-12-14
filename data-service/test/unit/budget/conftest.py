import pytest
from random import random, randint
from src.budget.container import BudgetContainer
from src.budget.models import Budget, FullBudgetModel
from test.unit.utils import model_factories


@pytest.fixture
def budget_container() -> BudgetContainer:
    return BudgetContainer()


@pytest.fixture
def budget_model() -> Budget:
    return model_factories.BudgetFactory.build()


@pytest.fixture
def full_budget_model() -> FullBudgetModel:
    return model_factories.FullBudgetModelFactory.build()


@pytest.fixture
def random_balance() -> float:
    return random()


@pytest.fixture
def random_year() -> int:
    return randint(1, 2000)
