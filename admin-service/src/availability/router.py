from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from src.availability.container import AvailabilityContainer
from src.availability.handler import AvailabilityHandler
from .models import (
    Availability,
    AvailabilityId,
    CreateAvailability
)


availability_router = APIRouter()


@availability_router.get("/availability/{availability_id}")
@inject
async def get_availability_by_id(
    availability_id: int,
    user_id: int,
    action_description: str,
    handler: AvailabilityHandler = Depends(Provide[AvailabilityContainer.handler])
) -> Availability:
    return await  handler.get_availability_by_id(
        availability_id=availability_id,
        user_id=user_id,
        action_description=action_description
    )


@availability_router.post("/availability")
@inject
async def create_availability(
    availability_body: CreateAvailability,
    user_id: int,
    action_description: str,
    handler: AvailabilityHandler = Depends(Provide[AvailabilityContainer.handler])
) -> AvailabilityId:
    return await handler.create_availability(
        availability_body=availability_body,
        user_id=user_id,
        action_description=action_description
    )


@availability_router.get("/availability")
@inject
async def get_availability_list_by_supply_id(
    supply_id: int ,
    user_id: int,
    action_description: str,
    handler: AvailabilityHandler = Depends(Provide[AvailabilityContainer.handler])
) -> list[Availability]:
    return await handler.get_availability_list_by_supply_id(
        supply_id=supply_id,
        user_id=user_id,
        action_description=action_description
    )

@availability_router.delete("/availability/{availability_id}")
@inject
async def delete_availability_by_id(
    availability_id: int,
    user_id: int,
    action_description: str,
    handler: AvailabilityHandler = Depends(Provide[AvailabilityContainer.handler])
) -> Availability:
    return await handler.delete_availability_by_id(
        availability_id=availability_id,
        user_id=user_id,
        action_description=action_description
    )
