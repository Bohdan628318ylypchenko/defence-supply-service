from datetime import date
from pydantic import BaseModel


class AvailabilityBase(BaseModel):
    supply_id: int
    unit_count: int
    expiration_date: date


class Availability(AvailabilityBase):
    id: int
    is_active: bool


class CreateAvailability(AvailabilityBase):
    pass


class AvailabilityId(BaseModel):
    id: int
