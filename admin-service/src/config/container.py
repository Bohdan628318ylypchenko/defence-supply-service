from dependency_injector import (
    containers,
    providers
)
from .models import (
    Postgres,
    Service
)


class Settings(containers.DeclarativeContainer):
    postgres = providers.Configuration(pydantic_settings=[Postgres()]) # type: ignore
    service = providers.Configuration(pydantic_settings=[Service()]) # type: ignore

