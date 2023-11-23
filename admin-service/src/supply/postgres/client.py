from loguru import logger
from databases import Database
from src.supply.models import Supply, SupplyId
from src.errors import exceptions
from . import queries


class SupplyClient:

    def __init__(
        self,
        db: Database
    ) -> None:
        self.__db = db

    async def get_supply_by_id(
        self,
        supply_id: int,
    ) -> Supply:
        logger.debug("SupplyClient started get_supply_by_id")
        values = {
            "supply_id": supply_id
        }
        supply_rec = await self.__db.fetch_one(
            query=queries.GET_SUPPLY_BY_ID,
            values=values   
        )
        if not supply_rec:
            logger.error(f"SupplyClient supply_id:{supply_id} not found")
            raise exceptions.SupplyNotFound
        logger.debug("SupplyClient returning Supply")
        return Supply.parse_obj(supply_rec)

    async def get_supply_by_name(
        self,
        name: str
    ) -> Supply:
        logger.debug("SupplyClient started get_supply_by_name")
        values = {
            "name" : name
        }
        supply_rec = await self.__db.fetch_one(
            query=queries.GET_SUPPLY_BY_NAME,
            values=values   
        )
        if not supply_rec:
            logger.error(f"SupplyClient name:{name} not found")
            raise exceptions.SupplyNotFound
        logger.debug("SupplyClient returning Supply")
        return Supply.parse_obj(supply_rec)

    async def create_supply(
        self,
        name: str,
        unit_cost: float,
        unit_type: str,
        norm_unit_count_day: float
    ) -> SupplyId:
        logger.debug("SupplyClient started creating Supply")
        values = {
            "name": name,
            "unit_cost": unit_cost,
            "unit_type": unit_type,
            "norm_unit_count_day": norm_unit_count_day,
            "is_active": True,
        }
        supply_id = await self.__db.execute(
            query=queries.CREATE_SUPPLY,
            values=values
        )
        if not supply_id:
            logger.error("SupplyClient failed to create Supply")
            raise exceptions.SupplyCreationFail
        logger.debug("SupplyClient returning Supply")
        return SupplyId(id=supply_id)
    
    async def delete_supply_by_id(
        self,
        supply_id: int
    ) -> Supply:
        logger.debug("SupplyClient started delete_supply_by_id")
        values = {
            "supply_id": supply_id,
            "is_active": False
        }
        async with self.__db.transaction():
            supply_rec = await self.__db.fetch_one(
                query=queries.DELETE_SUPPLY_BY_ID,
                values=values
            )
            if not supply_rec:
                logger.error(f"SupplyClient supply_id:{supply_id} not found")
                raise exceptions.SupplyNotFound
            await self.__db.execute(
                query=queries.DELETE_AVAILABILITY_BY_SUPPLY_ID,
                values=values
            )
        logger.debug("SupplyClient returning Supply")
        return Supply.parse_obj(supply_rec)

