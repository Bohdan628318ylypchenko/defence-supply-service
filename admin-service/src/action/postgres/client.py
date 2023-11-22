from datetime import datetime
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
        if not action_id:
            raise exceptions.ActionCreationFail
        return action_id

    async def create_supply_action(
        self,
        action_id: int,
        supply_id: int | None
    ) -> int | None: 
        values = {
            "action_id": action_id,
            "supply_id": supply_id
        }
        supply_action_supply_id = await self.__db.execute(
            query=queries.CREATE_SUPPLY_ACTION,
            values=values
        )
        if not supply_action_supply_id:
            return None
        return supply_action_supply_id

    async def set_status(
        self, 
        action_id: int,
        execution_status_id: int
    ) -> None:
        values = {
            "action_id": action_id,
            "execution_status": execution_status_id
        }
        await self.__db.execute(
            query=queries.SET_STATUS,
            values=values
        )

    async def get_execution_status_id(
        self,
        execution_status: ExecutionStatus
    ) -> int | None:
        values = {
            "status": execution_status
        }
        execution_status_rec = await self.__db.fetch_one(
            query=queries.GET_EXECUTION_STATUS_ID,
            values=values
        )
        if not execution_status_rec:
            return None
        return execution_status_rec["id"]
    
    async def get_action_type_id(
        self,
        action_type: ActionType
    ) -> int | None:
        values = {
            "type": action_type
        }
        action_type_rec = await self.__db.fetch_one(
            query=queries.GET_ACTION_TYPE_ID,
            values=values
        )
        if not action_type_rec:
            return None
        return action_type_rec["id"]
