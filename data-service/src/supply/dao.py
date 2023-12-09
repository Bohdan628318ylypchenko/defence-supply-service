from src.supply.models import FullSupplyModel, Supply
from .postgres.client import SupplyClient


class SupplyDAO:
    
    def __init__(
        self,
        db_client: SupplyClient
    ) -> None:
        self.__db_client = db_client

    async def import_supply(
        self,
        supply_list: list[Supply]
    ) -> None:
        await self.__db_client.import_supply(
            supply_list=supply_list
        )

    async def export_supply(
        self,
        unit_cost_min: float | None,
        unit_cost_max: float | None,
        unit_type: str | None,
        norm_unit_count_day_min: float | None,
        norm_unit_count_day_max: float | None
    ) -> list[FullSupplyModel]:
        return await self.__db_client.export_supply(
            unit_cost_min=unit_cost_min,
            unit_cost_max=unit_cost_max,
            unit_type=unit_type,
            norm_unit_count_day_min=norm_unit_count_day_min,
            norm_unit_count_day_max=norm_unit_count_day_max
        )
