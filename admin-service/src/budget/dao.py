from src.budget.models import Budget
from .postgres.client import BudgetClient


class BudgetDAO:

    def __init__(
        self,
        db_client: BudgetClient
    ) -> None:
        self.__db_client = db_client

    async def get_budget_by_id(
        self,
        budget_id: int
    ) -> Budget:
        return await self.__db_client.get_budget_by_id(
            budget_id
        )

    async def get_budget_by_year(
        self,
        year: int
    ) -> Budget:
        return await self.__db_client.get_budget_by_year(
            year=year
        )

    async def create_budget(
        self, 
        year: int,
        balance: float
    ) -> Budget:
        return await self.__db_client.create_budget(
            year=year,
            balance=balance
        )

    async def delete_budget_by_id(
        self,
        budget_id: int
    ) -> Budget:
        return await self.__db_client.delete_budget_by_id(
            budget_id=budget_id
        )

    async def delete_budget_by_year(
        self, 
        year: int
    ) -> Budget:
        return await self.__db_client.delete_budget_by_year(
            year=year
        )
