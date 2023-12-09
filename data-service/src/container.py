from dependency_injector import (
    containers,
    providers
)
from fastapi import FastAPI
from src.availability.container import AvailabilityContainer

from src.budget.container import BudgetContainer
from src.supply.container import SupplyContainer
from .config.container import Settings
from src.utils.db_utils import init_postgres


class Application(containers.DeclarativeContainer):
    config = providers.Container(Settings)
    database = providers.Resource(
        init_postgres,
        url=f"postgresql://{config.postgres.user()}:{config.postgres.password()}@"  # type: ignore
            f"{config.postgres.host()}:{config.postgres.port()}/{config.postgres.db_name()}"  # type: ignore
    )
    fastapi_app = providers.Singleton(FastAPI)
    budget = providers.Container(
        BudgetContainer,
        database=database
    )
    supply = providers.Container(
        SupplyContainer,
        database=database
    )
    availability = providers.Container(
        AvailabilityContainer,
        database=database
    )
