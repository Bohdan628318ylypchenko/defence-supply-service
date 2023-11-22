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
        values = {
            "supply_id": supply_id
        }
        supply_rec = await self.__db.fetch_one(
            query=queries.GET_SUPPLY_BY_ID,
            values=values   
        )
        if not supply_rec:
            raise exceptions.SupplyNotFound
        return Supply.parse_obj(supply_rec)

    async def get_supply_by_name(
        self,
        name: str
    ) -> Supply:
        values = {
            "name" : name
        }
        supply_rec = await self.__db.fetch_one(
            query=queries.GET_SUPPLY_BY_NAME,
            values=values   
        )
        if not supply_rec:
            raise exceptions.SupplyNotFound
        return Supply.parse_obj(supply_rec)

    async def create_supply(
        self,
        name: str,
        unit_cost: float,
        unit_type: str,
        norm_unit_count_day: float
    ) -> SupplyId:
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
            raise exceptions.SupplyCreationFail
        return SupplyId(id=supply_id)
    
    async def delete_supply_by_id(
        self,
        supply_id: int
    ) -> Supply:
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
                raise exceptions.SupplyNotFound
            await self.__db.execute(
                query=queries.DELETE_AVAILABILITY_BY_SUPPLY_ID,
                values=values
            )
        return Supply.parse_obj(supply_rec)

