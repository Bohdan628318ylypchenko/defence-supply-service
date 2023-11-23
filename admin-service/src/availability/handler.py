from src.action.handler import ActionHandler
from src.action.models import ActionType
from src.availability.models import (
    Availability,
    AvailabilityId,
    CreateAvailability
)
from src.errors.exceptions import CustomError
from src.utils.error_handler import raise_exception
from .dao import AvailabilityDAO


class AvailabilityHandler:

    def __init__(
        self,
        dao: AvailabilityDAO,
        action_handler: ActionHandler
    ) -> None:
        self.__dao = dao
        self.__action_handler = action_handler

    async def get_availability_by_id(
        self,
        availability_id: int,
        user_id: int,
        action_description: str
    ) -> Availability:
        try:
            action_id = await self.__action_handler.handle_action(
                user_id=user_id,
                action_description=action_description,
                action_type=ActionType.GET
            )
            availablity = await self.__dao.get_availability_by_id(
                availability_id=availability_id
            )
            availability_action_id = await self.__action_handler.create_availability_action(
                availability_id=availablity.id,
                action_id=action_id
            )
            await self.__action_handler.handle_execution_status(
                action_id=action_id,
                entity_id=availablity.id
            )
            return availablity
        except CustomError as error:
            raise_exception(exception=error)

    async def create_availability(
        self,
        availability_body: CreateAvailability,
        user_id: int,
        action_description: str
    ) -> AvailabilityId:
        try:
            action_id = await self.__action_handler.handle_action(
                user_id=user_id,
                action_description=action_description,
                action_type=ActionType.CREATE
            )
            availability_id = await self.__dao.create_availability(
                supply_id=availability_body.supply_id,
                unit_count=availability_body.unit_count,
                expiration_datetime=availability_body.expiration_datetime
            )
            availability_action_id = await self.__action_handler.create_availability_action(
                action_id=action_id,
                availability_id=availability_id.id
            )
            await self.__action_handler.handle_execution_status(
                action_id=action_id,
                entity_id=availability_id.id
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
        try:
            action_id = await self.__action_handler.handle_action(
                user_id=user_id,
                action_description=action_description,
                action_type=ActionType.GET,
            )
            availability_list = await self.__dao.get_availability_list_by_supply_id(
                supply_id=supply_id
            )
            for availability in availability_list:
                availability_action_ids = await self.__action_handler.create_availability_action(
                    action_id=action_id,
                    availability_id=availability.id
                )
                await self.__action_handler.handle_execution_status(
                    action_id=action_id,
                    entity_id=availability.id
                )
            return availability_list
        except CustomError as error:
            raise_exception(exception=error)

    async def delete_availability_by_id(
        self,
        availability_id: int, 
        user_id: int, 
        action_description: str
    ) -> Availability:
        try:
            action_id = await self.__action_handler.handle_action(
                user_id=user_id,
                action_description=action_description,
                action_type=ActionType.DELETE,
            )
            availability = await self.__dao.delete_availability_by_id(
                availability_id=availability_id
            )
            availability_action_id = await self.__action_handler.create_availability_action(
                action_id=action_id,
                availability_id=availability.id
            )
            await self.__action_handler.handle_execution_status(
                action_id=action_id,
                entity_id=availability.id
            )
            return availability
        except CustomError as error:
            raise_exception(exception=error)
