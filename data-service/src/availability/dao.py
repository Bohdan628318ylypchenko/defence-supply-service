from datetime import date
from .postgres.client import AvailabilityClient
from .models import Availability, FullAvailabilityModel


class AvailabilityDAO:

    def __init__(
        self,
        db_client: AvailabilityClient
    ) -> None:
        self.__db_client = db_client

    async def import_availability(
        self,
        availability_list: list[Availability]
    ) -> None:
        await self.__db_client.import_availability(
            availability_list=availability_list
        )

    async def export_availability(
        self,
        start_date: date | None,
        end_date: date | None,
        supply_id: int | None
    ) -> list[FullAvailabilityModel]:
        return await self.__db_client.export_availability(
            start_date=start_date,
            end_date=end_date,
            supply_id=supply_id
        )
