from dependency_injector import (
    containers,
    providers
)
from src.availability.postgres.client import AvailabilityClient
from src.availability.dao import AvailabilityDAO
from src.availability.handler import AvailabilityHandler


class AvailabilityContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".router"])
    
    database = providers.Dependency()
    action_handler = providers.Dependency()
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
        dao=dao,
        action_handler=action_handler
    )

