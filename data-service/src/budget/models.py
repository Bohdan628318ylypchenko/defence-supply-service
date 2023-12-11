from typing import Any
from pydantic import BaseModel, validator


class Budget(BaseModel):
    balance: float
    year: int
    is_active: bool = True

    @validator("year", pre=True, always=True)
    def convert_to_int(cls, data: Any) -> Any:
        if isinstance(data, str):
            return int(data)
        return data

    @validator("balance", pre=True, always=True)
    def convert_to_float(cls, data: Any) -> Any:
        if isinstance(data, str):
            return float(data)
        return data


class FullBudgetModel(BaseModel):
    id: int
    balance: float
    year: int
    is_active: bool
