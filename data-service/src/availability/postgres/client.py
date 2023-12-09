from datetime import date
from asyncpg.exceptions import ForeignKeyViolationError, NotNullViolationError
from databases import Database
from . import queries
from src.errors import exceptions
from src.availability.models import Availability, FullAvailabilityModel


class AvailabilityClient:

    def __init__(
        self,
        db: Database
    ) -> None:
        self.__db = db

    async def import_availability(
        self,
        availability_list: list[Availability]
    ) -> None:
        try:
            await self.__db.execute_many(
                query=queries.IMPORT_AVAILABILITY,
                values=[availability.dict() for availability in availability_list]
            )
        except (ForeignKeyViolationError, NotNullViolationError):
            raise exceptions.AvailabilityForeignKeyViolation

    async def export_availability(
        self, 
        start_date: date | None,
        end_date: date | None,
        supply_id: int | None
    ) -> list[FullAvailabilityModel]:
        values = {
            "start_date": start_date,
            "end_date": end_date,
            "supply_id": supply_id
        }
        availabilities_raw = await self.__db.fetch_all(
            query=queries.EXPORT_AVAILABILITY,
            values=values
        )
        return [FullAvailabilityModel.parse_obj(availability) for availability in availabilities_raw]
