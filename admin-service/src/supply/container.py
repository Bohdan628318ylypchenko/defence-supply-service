from dependency_injector import (
    containers,
    providers
)


class SupplyContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".router"])

