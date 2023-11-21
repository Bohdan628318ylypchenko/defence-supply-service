from dependency_injector import (
    containers,
    providers
)

from .postgres.client import ActionClient
from .dao import ActionDAO
from .handler import ActionHandler


class ActionContainer(containers.DeclarativeContainer):

    database = providers.Dependency()

    db_client = providers.Singleton(
        ActionClient,
        database=database
    )
    dao = providers.Factory(
        ActionDAO,
        db_client=db_client
    )
    handler = providers.Factory(
        ActionHandler,
        dao=dao
    )

