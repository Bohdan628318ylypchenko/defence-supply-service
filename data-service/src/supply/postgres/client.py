from loguru import logger
from databases import Database
from src.supply.models import FullSupplyModel, Supply
from asyncpg.exceptions import UniqueViolationError
from src.errors import exceptions
from . import queries


class SupplyClient:

    def __init__(
        self,
        db: Database
    ) -> None:
        self.__db = db

    async def import_supply(
        self,
        supply_list: list[Supply]
    ) -> None:
        try:
            logger.debug("SupplyClient started importing supply")
            await self.__db.execute_many(
                query=queries.IMPORT_SUPPLY,
                values=[item.dict() for item in supply_list]
            )
            logger.debug("SupplyClient finished importing supply")
        except UniqueViolationError:
            raise exceptions.SupplyUniqueViolationError

    async def export_supply(
        self,
        unit_cost_min: float | None,
        unit_cost_max: float | None,
        unit_type: str | None,
        norm_unit_count_day_min: float | None,
        norm_unit_count_day_max: float | None
    ) -> list[FullSupplyModel]:
        values = {
            "unit_cost_min": unit_cost_min,
            "unit_cost_max": unit_cost_max,
            "unit_type": unit_type,
            "norm_unit_count_day_min": norm_unit_count_day_min,
            "norm_unit_count_day_max": norm_unit_count_day_max
        }
        supplies_raw = await self.__db.fetch_all(
            query=queries.EXPORT_SUPPLY,
            values=values
        )
        return [FullSupplyModel.parse_obj(supply) for supply in supplies_raw]
