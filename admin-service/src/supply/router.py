from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from src.supply.container import SupplyContainer
from src.supply.handler import SupplyHandler
from .models import CreateSupply, Supply, SupplyId


supply_router = APIRouter()


@supply_router.get("/supply/{supply_id}")
@inject
async def get_supply_by_id(
    supply_id: int,
    user_id: int,
    action_description: str,
    handler: SupplyHandler = Depends(Provide[SupplyContainer.handler])
) -> Supply | None:
    return await handler.get_supply_by_id(
        supply_id=supply_id,
        user_id=user_id,
        action_description=action_description
    )


@supply_router.get("/supply")
@inject
async def get_supply_by_name(
    name: str,
    user_id: int,
    action_description: str,
    handler: SupplyHandler = Depends(Provide[SupplyContainer.handler])
) -> Supply | None:
    return await handler.get_supply_by_name(
        name=name,
        user_id=user_id,
        action_description=action_description
    )


@supply_router.post("/supply")
@inject
async def create_supply(
    supply_body: CreateSupply,
    handler: SupplyHandler = Depends(Provide[SupplyContainer.handler])
) -> SupplyId | None:
    return await handler.create_supply(supply_body=supply_body)


@supply_router.delete("/supply/{supply_id}")
@inject
async def delete_supply_by_id(
    supply_id: int,
    user_id: int,
    action_description: str,
    handler: SupplyHandler = Depends(Provide[SupplyContainer.handler])
) -> Supply | None:
    return await handler.delete_supply_by_id(
        supply_id=supply_id,
        user_id=user_id,
        action_description=action_description
    )

