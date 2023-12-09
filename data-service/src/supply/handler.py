from io import StringIO
import csv
from fastapi.responses import StreamingResponse
from src.errors import exceptions
from src.utils.error_handler import raise_exception
from .dao import SupplyDAO
from pydantic.error_wrappers import ValidationError
from .models import FullSupplyModel, Supply


class SupplyHandler:

    def __init__(
        self,
        dao: SupplyDAO
    ) -> None:
        self.__dao = dao

    async def import_supply(
        self,
        contents: list[str]
    ) -> None:
        try: 
            supply_list = await self.__parse_to_supply(contents=contents)
            await self.__dao.import_supply(
                supply_list=supply_list
            )
        except exceptions.CustomError as error:
            raise_exception(exception=error)

    async def __validate_header(self, header: list[str]) -> bool:
        if len(header) != 4:
            return False
        if "name" not in header or "unit_cost" not in header or "unit_type" not in header or "norm_unit_count_day" not in header:
            return False
        return True

    async def __parse_to_supply(self, contents: list[str]) -> list[Supply]:
        try:
            header = contents.pop(0)
            header = header.split(",")
            if not await self.__validate_header(header):
                raise exceptions.InvalidSupplyImportHeader
            supply_items = [tuple(map(lambda x: x, item.split(','))) for item in contents]
            supply_models = [Supply(**dict(zip(header, item))) for item in supply_items] # type: ignore
            return supply_models
        except ValidationError:
            raise exceptions.InvalidSupplyImportBody

    async def export_supply(
        self,
        unit_cost_min: float | None,
        unit_cost_max: float | None,
        unit_type: str | None,
        norm_unit_count_day_min: float | None,
        norm_unit_count_day_max: float | None
    ) -> StreamingResponse:
        supplies = await self.__dao.export_supply(
            unit_cost_min=unit_cost_min,
            unit_cost_max=unit_cost_max,
            unit_type=unit_type,
            norm_unit_count_day_min=norm_unit_count_day_min,
            norm_unit_count_day_max=norm_unit_count_day_max
        )
        return await self.__create_csv(
            supplies=supplies
        )

    async def __create_csv(
        self,
        supplies: list[FullSupplyModel]
    ) -> StreamingResponse:
        csv_buffer = StringIO()
        csv_writer = csv.writer(csv_buffer)

        header = ["id", "is_active", "unit_cost", "unit_type", "norm_unit_count_day"]
        csv_writer.writerow(header)

        for supply in supplies:
            row = [supply.id, supply.is_active, supply.unit_cost, supply.unit_type, supply.norm_unit_count_day] 
            csv_writer.writerow(row)

        csv_content = csv_buffer.getvalue()

        csv_buffer.close()
        return StreamingResponse(iter([csv_content]), media_type="text/csv", headers={"Content-Disposition": "attachment; filename=budgets.csv"})
