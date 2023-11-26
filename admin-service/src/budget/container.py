from dependency_injector import (
    containers,
    providers
)
from src.budget.dao import BudgetDAO
from src.budget.handler import BudgetHandler
from src.budget.postgres.client import BudgetClient


class BudgetContainer(containers.DeclarativeContainer):
    
    
    wiring_config = containers.WiringConfiguration(modules=[".router"])
    
    database = providers.Dependency()
    action_handler = providers.Dependency()
    db_client = providers.Singleton(
        BudgetClient,
        db=database
    )
    dao = providers.Factory(
        BudgetDAO,
        db_client=db_client
    )
    handler = providers.Factory(
        BudgetHandler,
        dao=dao,
        action_handler=action_handler
    )


