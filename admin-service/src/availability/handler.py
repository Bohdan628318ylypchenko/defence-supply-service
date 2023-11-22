from dependency_injector.wiring import wire
from src.availability.models import (
    Availability,
    AvailabilityId,
    CreateAvailability
)
from src.errors.exceptions import CustomError
from src.utils.error_handler import raise_exception
from .dao import AvailabilityDAO
from src.errors import http_exceptions


class AvailabilityHandler:

    def __init__(
        self,
        dao: AvailabilityDAO
    ) -> None:
        self.__dao = dao

    async def get_availability_by_id(
        self,
        availability_id: int,
        user_id: int,
        action_description: str
    ) -> Availability:
        # TODO: Add action handling
        try:
            availablity = await self.__dao.get_availability_by_id(
                availability_id=availability_id
            )
            return availablity
        except CustomError as error:
            raise_exception(exception=error)

    async def create_availability(
        self,
        availability_body: CreateAvailability
    ) -> AvailabilityId:
        try:
            availability_id = await self.__dao.create_availability(
                supply_id=availability_body.supply_id,
                unit_count=availability_body.unit_count,
                expiration_datetime=availability_body.expiration_datetime
            )
            return availability_id
        except CustomError as error:
            raise_exception(exception=error)

    async def get_availability_list_by_supply_id(
        self,
        supply_id: int,
        user_id: int,
        action_description: str
    ) -> list[Availability]:
        return await self.__dao.get_availability_list_by_supply_id(
            supply_id=supply_id
        )

    async def delete_availability_by_id(
        self,
        availability_id: int, 
        user_id: int, 
        action_description: str
    ) -> Availability:
        try:
            availability = await self.__dao.delete_availability_by_id(
                availability_id=availability_id
            )
            return availability
        except CustomError as error:
            raise_exception(exception=error)
