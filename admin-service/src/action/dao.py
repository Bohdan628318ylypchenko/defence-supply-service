from src.action.models import (
    ActionType,
    ExecutionStatus,
)
from .postgres.client import ActionClient



class ActionDAO:

    def __init__(
        self,
        db_client: ActionClient
    ) -> None:
        self.__db_client = db_client

    async def create_action(
        self, 
        user_id: int,
        action_type_id: int,
        action_description: str,
        execution_status: int 
    ) -> int:
        return await self.__db_client.create_action(
            user_id=user_id,
            action_type_id=action_type_id,
            action_description=action_description,
            execution_status=execution_status
        )
    
    async def create_availability_action(
        self,
        availability_id: int | None,
        action_id: int
    ) -> int:
        return await self.__db_client.create_availability_action(
            availability_id=availability_id,
            action_id=action_id
        )


    async def create_supply_action(
        self,
        supply_id: int | None,
        action_id: int
    ) -> int:
        return await self.__db_client.create_supply_action(
            supply_id=supply_id,
            action_id=action_id
        )

    async def create_budget_action(
        self,
        action_id: int,
        budget_id: int | None
    ) -> int:
        return await self.__db_client.create_budget_action(
            action_id=action_id,
            budget_id=budget_id
        )

    async def set_status(
        self,
        action_id: int,
        execution_status_id: int
    ) -> None:
        await self.__db_client.set_status(
            action_id=action_id,
            execution_status_id=execution_status_id
        )

    async def get_execution_status_id(
        self,
        execution_status: ExecutionStatus
    ) -> int:
        return await self.__db_client.get_execution_status_id(
            execution_status=execution_status
        )

    async def get_action_type_id(
        self,
        action_type: ActionType
    ) -> int:
        return await self.__db_client.get_action_type_id(
            action_type=action_type
        )
