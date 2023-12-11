from dependency_injector import (
    containers,
    providers
)
from .postgres.client import AvailabilityClient
from .dao import AvailabilityDAO
from .handler import AvailabilityHandler


class AvailabilityContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".router"])
    
    database = providers.Dependency()
    db_client = providers.Singleton(
        AvailabilityClient,
        db=database
    )
    dao = providers.Factory(
        AvailabilityDAO,
        db_client=db_client
    )
    handler = providers.Factory(
        AvailabilityHandler,
        dao=dao
    )

