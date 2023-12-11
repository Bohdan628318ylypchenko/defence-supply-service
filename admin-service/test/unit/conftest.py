import random
import pytest 


@pytest.fixture
def action_id() -> int: 
    return random.randint(1, 100)


@pytest.fixture
def user_id() -> int:
    return random.randint(1, 100)


@pytest.fixture
def action_description() -> str:
    return "action_description"
