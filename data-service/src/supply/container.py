from dependency_injector import (
    containers,
    providers
)
from .postgres.client import SupplyClient
from .dao import SupplyDAO
from .handler import SupplyHandler
    

class SupplyContainer(containers.DeclarativeContainer):
    wiring_config  = containers.WiringConfiguration(modules=[".router"])

    database = providers.Dependency()
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
        dao=dao
    )

