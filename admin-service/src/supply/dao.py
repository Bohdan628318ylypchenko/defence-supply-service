from src.supply.models import CreateSupply, Supply, SupplyId
from src.supply.postgres.client import SupplyClient


class SupplyDAO:

    def __init__(
        self,
        db_client: SupplyClient
    ) -> None:
        self.__db_client = db_client 

    async def get_supply_by_id(
        self,
        supply_id: int,
    ) -> Supply:
        return await self.__db_client.get_supply_by_id(
            supply_id=supply_id,
        )

    async def get_supply_by_name(
        self, 
        name: str,
    ) -> Supply:
        return await self.__db_client.get_supply_by_name(
            name=name,
        )

    async def create_supply(
        self, 
        name: str,
        unit_cost: float,
        unit_type: str,
        norm_unit_count_day: float
    ) -> SupplyId:
        return await self.__db_client.create_supply(
            name=name,
            unit_cost=unit_cost,
            unit_type=unit_type,
            norm_unit_count_day=norm_unit_count_day
        )

    async def delete_supply_by_id(
        self, 
        supply_id: int
    ) -> Supply:
        return await self.__db_client.delete_supply_by_id(
            supply_id=supply_id
        )
