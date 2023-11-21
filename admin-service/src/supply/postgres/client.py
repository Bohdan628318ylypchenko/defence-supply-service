from databases import Database
from src.supply.models import Supply, SupplyId
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
    ) -> Supply | None:
        values = {
            "supply_id": supply_id
        }
        supply_rec = await self.__db.fetch_one(
            query=queries.GET_SUPPLY_BY_ID,
            values=values   
        )
        if supply_rec:
            return Supply.parse_obj(supply_rec)
        return None

    async def get_supply_by_name(
        self,
        name: str
    ) -> Supply | None:
        values = {
            "name" : name
        }
        supply_rec = await self.__db.fetch_one(
            query=queries.GET_SUPPLY_BY_NAME,
            values=values   
        )
        if supply_rec:
            return Supply.parse_obj(supply_rec)
        return None 

    async def create_supply(
        self,
        name: str,
        unit_cost: float,
        unit_type: str,
        norm_unit_count_day: float
    ) -> SupplyId | None:
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
        if supply_id:
            return SupplyId(id=supply_id)
        return None
    
    async def delete_supply_by_id(
        self,
        supply_id: int
    ) -> Supply | None:
        values = {
            "supply_id": supply_id,
            "is_active": False
        }
        supply_rec = await self.__db.fetch_one(
            query=queries.DELETE_SUPPLY_BY_ID,
            values=values
        )
        if not supply_rec:
            return None
        return Supply.parse_obj(supply_rec)

