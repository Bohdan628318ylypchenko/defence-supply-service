from loguru import logger
from databases import Database
from datetime import datetime

from src.availability.models import Availability, AvailabilityId
from . import queries


class AvailabilityClient:

    def __init__(
        self,
        db: Database
    ) -> None:
        self.__db = db 

    async def get_availability_by_id(
        self,
        availability_id: int
    ) -> Availability | None:
        values = {
            "availability_id": availability_id 
        }
        availability_rec = await self.__db.fetch_one(
            query=queries.GET_AVAILABILITY_BY_ID,
            values=values
        )
        if availability_rec:
            return Availability.parse_obj(availability_rec)
        return None 
    
    async def create_availability(
        self, 
        supply_id: int,
        unit_count: int,
        expiration_datetime: datetime
    ) -> AvailabilityId | None:
        values = {
            "supply_id": supply_id,
            "is_active": True,
            "unit_count": unit_count,
            "expiration_datetime": expiration_datetime
        }
        availability_id = await self.__db.execute(
            query=queries.CREATE_AVAILABILITY,
            values=values
        )
        if not availability_id:
            return None
        return AvailabilityId(id=availability_id)

    async def get_availability_list_by_supply_id(
        self,
        supply_id: int
    ) -> list[Availability]:
        values = {
            "supply_id": supply_id
        }
        availability_rec_list = await self.__db.fetch_all(
            query=queries.GET_AVAILABILITY_LIST_BY_SUPPLY_ID,
            values=values
        )
        return [Availability.parse_obj(availability_rec) for availability_rec in availability_rec_list]

    async def delete_availability_by_id(
        self, 
        availability_id: int
    ) -> Availability | None:
        values = {
            "availability_id": availability_id,
            "is_active": False
        }
        availability_rec = await self.__db.fetch_one(
            query=queries.DELETE_AVAILABILITY_BY_ID,
            values=values
        )
        logger.debug(f"Got Availability {availability_rec}")
        if not availability_rec:
            return None
        return Availability.parse_obj(availability_rec)
