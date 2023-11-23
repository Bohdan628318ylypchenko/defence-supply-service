from asyncpg import ForeignKeyViolationError
from loguru import logger
from databases import Database
from datetime import datetime
from src.availability.models import Availability, AvailabilityId
from src.errors import exceptions
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
    ) -> Availability:
        logger.debug("AvailabilityClient started get_availability_by_id")
        values = {
            "availability_id": availability_id 
        }
        availability_rec = await self.__db.fetch_one(
            query=queries.GET_AVAILABILITY_BY_ID,
            values=values
        )
        if not availability_rec:
            logger.error(f"AvailabilityClient availiablity_id:{availability_id} not found")
            raise exceptions.AvailabilityNotFound
        logger.debug("AvailabilityClient returning Availability")
        return Availability.parse_obj(availability_rec)

    async def create_availability(
        self, 
        supply_id: int,
        unit_count: int,
        expiration_datetime: datetime
    ) -> AvailabilityId:
        try:
            logger.debug("AvailabilityClient started creating availability")
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
            logger.debug("AvailabilityClient returning Availability")
            return AvailabilityId(id=availability_id)
        except ForeignKeyViolationError:
            logger.error("AvailabilityClient failed to create availability")
            raise exceptions.AvailabilityCreationFail

    async def get_availability_list_by_supply_id(
        self,
        supply_id: int
    ) -> list[Availability]:
        logger.debug("AvailabilityClient started get_availability_list_by_supply_id")
        values = {
            "supply_id": supply_id
        }
        availability_rec_list = await self.__db.fetch_all(
            query=queries.GET_AVAILABILITY_LIST_BY_SUPPLY_ID,
            values=values
        )
        logger.debug("AvailabilityClient returning get_availability_list_by_supply_id")
        return [Availability.parse_obj(availability_rec) for availability_rec in availability_rec_list]

    async def delete_availability_by_id(
        self, 
        availability_id: int
    ) -> Availability:
        logger.debug("AvailabilityClient started deleting availability")
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
            logger.error(f"AvailabilityClient availiablity_id:{availability_id} not found")
            raise exceptions.AvailabilityNotFound
        logger.debug("AvailabilityClient returning Availability")
        return Availability.parse_obj(availability_rec)
