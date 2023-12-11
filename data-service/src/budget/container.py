from dependency_injector import (
    containers,
    providers
)

from src.budget.handler import BudgetImportHandler
from src.budget.dao import BudgetImportDAO
from src.budget.postgres.client import BudgetImportClient


class BudgetContainer(containers.DeclarativeContainer):
    wiring_config  = containers.WiringConfiguration(modules=[".router"])

    database = providers.Dependency()
    db_client = providers.Singleton(
        BudgetImportClient,
        db=database
    )
    dao = providers.Factory(
        BudgetImportDAO,
        db_client=db_client
    )
    handler = providers.Factory(
        BudgetImportHandler,
        dao=dao
    )

