from datetime import date
from src.availability.models import (
    Availability,
    AvailabilityId
)
from src.availability.postgres.client import AvailabilityClient


class AvailabilityDAO:

    def __init__(
        self,
        db_client: AvailabilityClient
    ) -> None:
        self.__db_client = db_client 

    async def get_availability_by_id(
        self,
        availability_id: int
    ) -> Availability:
        return await self.__db_client.get_availability_by_id(
            availability_id=availability_id
        )

    async def create_availability(
        self, 
        supply_id: int,
        unit_count: int,
        expiration_date: date
    ) -> AvailabilityId:
        return await self.__db_client.create_availability(
            supply_id=supply_id,
            unit_count=unit_count,
            expiration_date=expiration_date
        )

    async def get_availability_list_by_supply_id(
        self,
        supply_id: int
    ) -> list[Availability]:
        return await self.__db_client.get_availability_list_by_supply_id(
            supply_id=supply_id
        )

    async def delete_availability_by_id(
        self,
        availability_id: int
    ) -> Availability:
        return await self.__db_client.delete_availability_by_id(
            availability_id=availability_id
        )
