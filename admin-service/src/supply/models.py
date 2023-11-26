from pydantic import BaseModel


class SupplyBase(BaseModel):
    name: str
    unit_cost: float
    unit_type: str
    norm_unit_count_day: float


class Supply(SupplyBase):
    id: int
    is_active: bool


class CreateSupply(SupplyBase):
    pass


class SupplyId(BaseModel):
    id: int 

