import pytest
from random import randint
from src.action.container import ActionContainer


@pytest.fixture
def action_container() -> ActionContainer:
    return ActionContainer()


@pytest.fixture
def execution_status() -> int:
    return randint(1, 100)


@pytest.fixture
def action_type_id() -> int:
    return randint(1, 100)


@pytest.fixture
def entity_id() -> int:
    return randint(1, 100)


@pytest.fixture
def entity_action_id() -> int:
    return randint(1, 100)
