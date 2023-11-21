from databases import Database
from . import queries
from src.budget.models import Budget
from src.errors import exceptions


class BudgetClient:

    def __init__(
        self,
        db: Database
    ) -> None:
        self.__db = db

    async def get_budget_by_id(
        self,
        budget_id: int
    ) -> Budget:
        values = {
            "budget_id": budget_id
        }
        res = await self.__db.fetch_one(
            query=queries.GET_BUDGET_BY_ID,
            values=values
        )
        if not res:
            raise exceptions.BudgetNotFound
        return Budget.parse_obj(res)

    async def get_budget_by_year(
        self,
        year: int
    ) -> Budget:
        values = {
            "year": year
        }
        res = await self.__db.fetch_one(
            query=queries.GET_BUDGET_BY_YEAR,
            values=values
        )
        if not res:
            raise exceptions.BudgetNotFound
        return Budget.parse_obj(res)

    async def create_budget(
        self,
        year: int,
        balance: float
    ) -> Budget:
        values = {
            "is_active": True,
            "balance": balance,
            "year": year
        }
        res = await self.__db.fetch_one(
            query=queries.CREATE_BUDGET,
            values=values
        )
        if not res:
            raise exceptions.BudgetCreationFail
        return Budget.parse_obj(res)

    async def delete_budget_by_id(
        self, 
        budget_id: int
    ) -> Budget:
        values = {
            "budget_id": budget_id,
            "is_active": False
        }
        res = await self.__db.fetch_one(
            query=queries.DELETE_BUDGET_BY_ID,
            values=values
        )
        if not res:
            raise exceptions.BudgetNotFound
        return Budget.parse_obj(res)

    async def delete_budget_by_year(
        self,
        year: int
    ) -> Budget:
        values = {
            "year": year,
            "is_active": False
        }
        res = await self.__db.fetch_one(
            query=queries.DELETE_BUDGET_BY_YEAR,
            values=values
        )
        if not res:
            raise exceptions.BudgetNotFound
        return Budget.parse_obj(res)
