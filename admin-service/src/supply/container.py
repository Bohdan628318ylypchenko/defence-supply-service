from dependency_injector import (
    containers,
    providers
)
from src.supply.dao import SupplyDAO
from src.supply.handler import SupplyHandler
from src.supply.postgres.client import SupplyClient


class SupplyContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".router"])
    
    database = providers.Dependency()
    action_handler = providers.Dependency()
    db_client = providers.Singleton(
        SupplyClient,
        db=database
    )
    dao = providers.Factory(
        SupplyDAO,
        db_client=db_client
    )
    handler = providers.Factory(
        SupplyHandler,
        dao=dao,
        action_handler=action_handler
    )

