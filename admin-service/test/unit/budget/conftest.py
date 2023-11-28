import random
import pytest
from src.budget.container import BudgetContainer
from src.budget.models import Budget, CreateBudget
from test.unit.utils import model_factories


@pytest.fixture
def budget_container() -> BudgetContainer:
    return BudgetContainer()


@pytest.fixture
def budget_model() -> Budget:
    return model_factories.BudgetFactory.build()


@pytest.fixture
def budget_action_id() -> int:
    return random.randint(1, 100)


@pytest.fixture
def create_budget_model(
    budget_model: Budget
) -> CreateBudget:
    create_budget_model = model_factories.CreateBudgetFactory.build()
    create_budget_model.year = budget_model.year,
    create_budget_model.balance = budget_model.balance
    return create_budget_model

