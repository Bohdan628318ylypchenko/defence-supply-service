from loguru import logger

from src.errors.exceptions import CustomError
from src.utils.error_handler import raise_exception
from .dao import ActionDAO
from .models import (
    ActionType,
    EntityAction,
    ExecutionStatus,
)
from src.errors import http_exceptions


class ActionHandler:

    def __init__(
        self,
        dao: ActionDAO
    ) -> None:
        self.__dao = dao

    async def handle_action(
        self,
        action_type: ActionType,
        user_id: int,
        action_description: str,
        entity_action:  EntityAction,
    ) -> int: #type: ignore
        if entity_action is EntityAction.SUPPLY_ACTION:
            return await self.__handle_supply_action(
                action_type=action_type,
                user_id=user_id,
                action_description=action_description,
            )
        if entity_action is EntityAction.AVAILABILITY_ACTION:
            return await self.__handle_availability_action(
                action_type=action_type,
                user_id=user_id,
                action_description=action_description
            )

    async def __handle_availability_action(
        self,
        action_type: ActionType,
        user_id: user_id,
        action_description: str
    ) -> int:
        ...
        
    async def __handle_supply_action(
        self, 
        action_type: ActionType,
        user_id: int,
        action_description: str
    ) -> int:
        try:
            action_type_id = await self.__dao.get_action_type_id(action_type=action_type)
            execution_status = await self.__dao.get_execution_status_id(
                execution_status=ExecutionStatus.IN_PROGRESS
            )
            action_id = await self.__dao.create_action(
                user_id=user_id,
                action_type_id=action_type_id,
                action_description=action_description,
                execution_status=execution_status
            )
            return action_id
        except CustomError as error:
            raise_exception(exception=error)

    async def create_supply_action(
        self,
        action_id: int,
        supply_id: int | None
    ) -> int | None:
        supply_action_supply_id = await self.__dao.create_supply_action(
            action_id=action_id,
            supply_id=supply_id
        )
        if not supply_action_supply_id:
            logger.error(f"Failed to create SupplyAction for action_id:{action_id}, supply_id:{supply_id}")
        return supply_action_supply_id

    async def handle_execution_status(
        self,
        action_id: int,
        entity_id: int | None
    ) -> None:
        if not entity_id:
            execution_status_id = await self.__dao.get_execution_status_id(
                execution_status=ExecutionStatus.FAIL
            )
            return await self.__dao.set_status(
                action_id=action_id,
                execution_status_id=execution_status_id
            )
        execution_status_id = await self.__dao.get_execution_status_id(
            execution_status=ExecutionStatus.SUCCESS
        )
        return await self.__dao.set_status(
            action_id=action_id,
            execution_status_id=execution_status_id
        )

