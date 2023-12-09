from pydantic import BaseModel


class Supply(BaseModel):
    is_active: bool = True
    name: str 
    unit_cost: float
    unit_type: str
    norm_unit_count_day: float


class FullSupplyModel(Supply):
    id: int
