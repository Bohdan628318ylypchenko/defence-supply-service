from pydantic import BaseModel


class BudgetBase(BaseModel):
    balance: float
    year: int


class Budget(BudgetBase):
    id: int
    is_active: bool


class CreateBudget(BudgetBase):
    user_id: int
    action_description: str
