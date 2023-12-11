from datetime import date
from pydantic import BaseModel


class Availability(BaseModel):
    is_active: bool = True
    supply_name: str
    unit_count: int
    expiration_date: date


class FullAvailabilityModel(Availability):
    id: int
    is_active: bool
