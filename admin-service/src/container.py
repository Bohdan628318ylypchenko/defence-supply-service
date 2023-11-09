from dependency_injector import (
    containers,
    providers
)
from fastapi import FastAPI
from .config.container import Settings
from src.supply.container import SupplyContainer


class Application(containers.DeclarativeContainer):
    config = providers.Container(Settings)
    fastapi_app = providers.Singleton(FastAPI)
    supply = providers.Container(SupplyContainer)
