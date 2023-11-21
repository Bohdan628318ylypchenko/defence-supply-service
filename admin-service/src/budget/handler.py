from src.budget.models import Budget, CreateBudget
from .dao import BudgetDAO
from src.errors.exceptions import CustomError
from src.utils.error_handler import raise_exception


class BudgetHandler:

    def __init__(
        self,
        dao: BudgetDAO
    ) -> None:
        self.__dao = dao

    async def get_budget_by_id(
        self,
        budget_id: int,
        user_id: int,
        action_description: str
    ) -> Budget:
        try:
            budget = await self.__dao.get_budget_by_id(
                budget_id=budget_id
            )
            return budget
        except CustomError as error:
            raise_exception(exception=error)

    async def get_budget_by_year(
        self,
        year: int,
        user_id: int,
        action_description: str
    ) -> Budget:
        try: 
            budget = await self.__dao.get_budget_by_year(
                year=year
            )
            return budget
        except CustomError as error:
            raise_exception(exception=error)

    async def create_budget(
        self,
        budget_body: CreateBudget
    ) -> Budget:
        try:
            budget = await self.__dao.create_budget(
                balance=budget_body.balance,
                year=budget_body.year
            )
            return budget
        except CustomError as error:
            raise_exception(exception=error)

    async def delete_budget_by_id(
        self,
        budget_id: int,
        user_id: int,
        action_description: str
    ) -> Budget:
        try:
            budget = await self.__dao.delete_budget_by_id(
                budget_id=budget_id
            )
            return budget
        except CustomError as error:
            raise_exception(exception=error)

    async def delete_budget_by_year(
        self, 
        year: int,
        user_id: int,
        action_description: str
    ) -> Budget:
        try: 
            budget = await self.__dao.delete_budget_by_year(
                year=year
            )
            return budget
        except CustomError as error:
            raise_exception(exception=error)
