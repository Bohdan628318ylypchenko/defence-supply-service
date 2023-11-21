from src.action.handler import ActionHandler
from src.action.models import (
    EntityAction,
    ActionType,
) 
from src.supply.dao import SupplyDAO
from src.supply.models import (
    CreateSupply, 
    Supply,
    SupplyId
)
from src.errors import http_exceptions


class SupplyHandler:

    def __init__(
        self,
        dao: SupplyDAO,
        action_handler: ActionHandler
    ) -> None:
        self.__dao = dao 
        self.__action_handler = action_handler

    async def get_supply_by_id(
        self,
        supply_id: int,
        user_id: int,
        action_description: str
    ) -> Supply | None:
        action_id = await self.__action_handler.handle_action(
            user_id=user_id,
            action_description=action_description,
            entity_action=EntityAction.SUPPLY_ACTION,
            action_type=ActionType.GET,
        )
        supply = await self.__dao.get_supply_by_id(
            supply_id=supply_id
        )
        supply_action_supply_id = await self.__action_handler.create_supply_action(
            action_id=action_id,
            supply_id=supply.id if supply else None
        )
        await self.__action_handler.handle_execution_status(
            action_id=action_id,
            entity_id=supply_action_supply_id
        )
        if not supply:
            raise http_exceptions.SUPPLY_NOT_FOUND
        return supply

    async def get_supply_by_name(
        self, 
        name: str,
        user_id: int,
        action_description: str
    ) -> Supply | None:
        action_id = await self.__action_handler.handle_action(
            user_id=user_id,
            action_description=action_description,
            entity_action=EntityAction.SUPPLY_ACTION,
            action_type=ActionType.GET,
        )
        supply = await self.__dao.get_supply_by_name(
            name=name
        )
        supply_action_supply_id = await self.__action_handler.create_supply_action(
            action_id=action_id,
            supply_id=supply.id if supply else None
        )
        await self.__action_handler.handle_execution_status(
            action_id=action_id,
            entity_id=supply_action_supply_id
        )
        if not supply:
            raise http_exceptions.SUPPLY_NOT_FOUND
        return supply

    async def create_supply(
        self,
        supply_body: CreateSupply
    ) -> SupplyId | None:
        action_id = await self.__action_handler.handle_action(
            user_id=supply_body.user_id,
            action_description=supply_body.action_description,
            entity_action=EntityAction.SUPPLY_ACTION,
            action_type=ActionType.CREATE,
        )   
        supply = await self.__dao.create_supply(
            name=supply_body.name,
            unit_cost=supply_body.unit_cost,
            unit_type=supply_body.unit_type,
            norm_unit_count_day=supply_body.norm_unit_count_day
        )
        supply_action_supply_id = await self.__action_handler.create_supply_action(
            action_id=action_id,
            supply_id=supply.id if supply else None
        )
        await self.__action_handler.handle_execution_status(
            action_id=action_id,
            entity_id=supply_action_supply_id
        )
        if not supply:
            raise http_exceptions.SUPPLY_CREATION_FAIL
        return supply

    async def delete_supply_by_id(
        self,
        supply_id: int,
        user_id: int,
        action_description: str
    ) -> Supply | None:
        action_id = await self.__action_handler.handle_action(
            user_id=user_id,
            action_description=action_description,
            entity_action=EntityAction.SUPPLY_ACTION,
            action_type=ActionType.DELETE,
        ) 
        supply = await self.__dao.delete_supply_by_id(
            supply_id=supply_id
        )
        supply_action_supply_id = await self.__action_handler.create_supply_action(
            action_id=action_id,
            supply_id=supply.id if supply else None
        )
        await self.__action_handler.handle_execution_status(
            action_id=action_id,
            entity_id=supply_action_supply_id
        )
        if not supply:
            raise http_exceptions.SUPPLY_NOT_FOUND
        return supply 

