from io import StringIO
import csv
from datetime import date
from fastapi.responses import StreamingResponse
from pydantic.error_wrappers import ValidationError
from .dao import AvailabilityDAO
from .models import Availability, FullAvailabilityModel
from src.errors import exceptions
from src.utils.error_handler import raise_exception


class AvailabilityHandler:

    def __init__(
        self,
        dao: AvailabilityDAO
    ) -> None:
        self.__dao = dao

    async def import_availability(
        self,
        contents: list[str]
    ) -> None:
        try:
            availability_list = await self.__parse_to_availability(contents=contents)
            await self.__dao.import_availability(
                availability_list=availability_list
            )
        except exceptions.CustomError as error:
            raise_exception(exception=error)

    async def __validate_header(self, header) -> bool:
        if len(header) != 3:
            return False
        if "supply_name" not in header or "unit_count" not in header or "expiration_date" not in header:
            return False
        return True


    async def __parse_to_availability(self, contents: list[str]) -> list[Availability]:
        try:
            header = contents.pop(0)
            header = header.split(",")
            if not await self.__validate_header(header):
                raise exceptions.InvalidAvailabilityImportHeader
            availability_items = [tuple(map(lambda x: x, item.split(','))) for item in contents]
            availability_models = [Availability(**dict(zip(header, item))) for item in availability_items] # type: ignore
            return availability_models
        except ValidationError:
            raise exceptions.InvalidAvailabilityImportBody

    async def export_availability(
        self,
        start_date: date | None,
        end_date: date | None,
        supply_id: int | None
    ) -> StreamingResponse:
        availabilities = await self.__dao.export_availability(
            start_date=start_date,
            end_date=end_date,
            supply_id=supply_id
        )
        return await self.__create_csv(
            availabilities=availabilities
        )

    async def __create_csv(
        self,
        availabilities: list[FullAvailabilityModel]
    ) -> StreamingResponse:

        csv_buffer = StringIO()
        csv_writer = csv.writer(csv_buffer)

        header = ["id", "is_active", "expiration_date", "unit_count", "supply_name"]
        csv_writer.writerow(header)

        for availability in availabilities:
            row = [availability.id, availability.is_active, availability.expiration_date, availability.unit_count, availability.supply_name] 
            csv_writer.writerow(row)

        csv_content = csv_buffer.getvalue()

        csv_buffer.close()
        return StreamingResponse(iter([csv_content]), media_type="text/csv", headers={"Content-Disposition": "attachment; filename=availabilities.csv"})
