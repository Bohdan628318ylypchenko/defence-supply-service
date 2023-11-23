from datetime import datetime
from pydantic import BaseModel


class AvailabilityBase(BaseModel):
    supply_id: int
    unit_count: int
    expiration_datetime: datetime


class Availability(AvailabilityBase):
    id: int
    is_active: bool


class CreateAvailability(AvailabilityBase):
    pass


class AvailabilityId(BaseModel):
    id: int
