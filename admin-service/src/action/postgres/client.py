from loguru import logger
from datetime import datetime
from asyncpg import ForeignKeyViolationError
from databases import Database
from src.action.models import (
    ActionType,
    ExecutionStatus,
)
from . import queries
from src.errors import exceptions


class ActionClient:

    def __init__(
        self,
        database: Database
    ) -> None:
        self.__db = database

    async def create_action(
        self,
        user_id: int,
        action_type_id: int,
        action_description: str,
        execution_status: int
    ) -> int:
        try:
            logger.debug("ActionClient started creating action")
            values = {
                "user_id": user_id,
                "type": action_type_id,
                "description": action_description,
                "start_datetime": datetime.now(),
                "execution_status": execution_status
            }
            action_id = await self.__db.execute(
                query=queries.CREATE_ACTION,
                values=values
            )
            logger.debug(f"ActionClient returning action_id:{action_id}")
            return action_id
        except ForeignKeyViolationError:
            logger.error("ActionClient failed to create action")
            raise exceptions.ActionCreationFail

    async def create_availability_action(
        self,
        action_id: int,
        availability_id: int | None
    ) -> int:
        try: 
            logger.debug("ActionClient started creating availability action")
            values = {
                "action_id": action_id,
                "availability_id": availability_id
            }
            availability_action_id = await self.__db.execute(
                query=queries.CREATE_AVAILABILITY_ACTION,
                values=values
            )
            logger.debug(f"ActionClient returnin availability_action_id:{availability_action_id}")
            return availability_action_id
        except ForeignKeyViolationError:
            logger.error("ActionClient failed to create availability action")
            raise exceptions.CreateAvailabilityActionFail

    async def create_supply_action(
        self,
        action_id: int,
        supply_id: int | None
    ) -> int: 
        try:
            logger.debug("ActionClient started creating supply action")
            values = {
                "action_id": action_id,
                "supply_id": supply_id
            }
            supply_action_id = await self.__db.execute(
                query=queries.CREATE_SUPPLY_ACTION,
                values=values
            )
            logger.debug(f"ActionClient returning supply_action_id:{supply_action_id}")
            return supply_action_id
        except ForeignKeyViolationError:
            logger.error("ActionClient failed to create supply action")
            raise exceptions.CreateSupplyActionFail

    async def create_budget_action(
        self,
        action_id: int,
        budget_id: int | None
    ) -> int:
        try:
            logger.debug("ActionClient started creating budget action")
            values = {
                "action_id": action_id,
                "budget_id": budget_id
            }
            budget_action_id = await self.__db.execute(
                query=queries.CREATE_BUDGET_ACTION,
                values=values
            )
            logger.debug(f"ActionClient returning budget_action_id:{budget_action_id}")
            return budget_action_id
        except ForeignKeyViolationError:
            logger.error("ActionClient failed to create supply action")
            raise exceptions.CreateBudgetActionFail

    async def set_status(
        self, 
        action_id: int,
        execution_status_id: int
    ) -> None:
        try:
            logger.debug(f"ActionClient started setting action_id:{action_id} status to status_id:{execution_status_id}")
            values = {
                "action_id": action_id,
                "execution_status": execution_status_id
            }
            await self.__db.execute(
                query=queries.SET_STATUS,
                values=values
            )
            logger.debug("ActionClient successfuly changed status")
        except ForeignKeyViolationError:
            logger.error("ActionClient failed changing execution status")
            raise exceptions.StatusUpdateError

    async def get_execution_status_id(
        self,
        execution_status: ExecutionStatus
    ) -> int:
        values = {
            "status": execution_status
        }
        execution_status_rec = await self.__db.fetch_one(
            query=queries.GET_EXECUTION_STATUS_ID,
            values=values
        )
        if not execution_status_rec:
            raise exceptions.ExecutionStatusNotFound
        return execution_status_rec["id"]
    
    async def get_action_type_id(
        self,
        action_type: ActionType
    ) -> int:
        values = {
            "type": action_type
        }
        action_type_rec = await self.__db.fetch_one(
            query=queries.GET_ACTION_TYPE_ID,
            values=values
        )
        if not action_type_rec:
            raise exceptions.ActionTypeNotFound
        return action_type_rec["id"]
