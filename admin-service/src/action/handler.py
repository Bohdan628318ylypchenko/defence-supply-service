from src.errors.exceptions import CustomError
from src.utils.error_handler import raise_exception
from .dao import ActionDAO
from .models import (
    ActionType,
    ExecutionStatus,
)


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
    ) -> int: 
        return await self.__create_action(
            action_type=action_type,
            user_id=user_id,
            action_description=action_description,
        )

    async def __create_action(
        self, 
        action_type: ActionType,
        user_id: int,
        action_description: str
    ) -> int:
        try:
            action_type_id = await self.__dao.get_action_type_id(action_type=action_type)
            execution_status = await self.__dao.get_execution_status_id(
                execution_status=ExecutionStatus.FAIL
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

    async def create_availability_action(
        self,
        action_id: int,
        availability_id: int | None
    ) -> int:
        return await self.__dao.create_availability_action(
            action_id=action_id,
            availability_id=availability_id
        )

    async def create_supply_action(
        self,
        action_id: int,
        supply_id: int | None
    ) -> int:
        supply_action_supply_id = await self.__dao.create_supply_action(
            action_id=action_id,
            supply_id=supply_id
        )
        return supply_action_supply_id

    async def create_budget_action(
        self,
        action_id: int,
        budget_id: int
    ) -> int | None:
        return await self.__dao.create_budget_action(
            action_id=action_id,
            budget_id=budget_id
        )


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

