from src.action.handler import ActionHandler
from src.action.models import ActionType
from src.budget.models import Budget, CreateBudget
from .dao import BudgetDAO
from src.errors.exceptions import CustomError
from src.utils.error_handler import raise_exception


class BudgetHandler:

    def __init__(
        self,
        dao: BudgetDAO,
        action_handler: ActionHandler
    ) -> None:
        self.__dao = dao
        self.__action_handler = action_handler

    async def get_budget_by_id(
        self,
        budget_id: int,
        user_id: int,
        action_description: str
    ) -> Budget:
        try:
            action_id = await self.__action_handler.handle_action(
                user_id=user_id,
                action_description=action_description,
                action_type=ActionType.GET
            )
            budget = await self.__dao.get_budget_by_id(
                budget_id=budget_id
            )
            budget_action_id = await self.__action_handler.create_budget_action(
                budget_id=budget.id,
                action_id=action_id
            )
            await self.__action_handler.handle_execution_status(
                action_id=action_id,
                entity_id=budget.id
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
            action_id = await self.__action_handler.handle_action(
                user_id=user_id,
                action_description=action_description,
                action_type=ActionType.GET
            )
            budget = await self.__dao.get_budget_by_year(
                year=year
            )
            budget_action_id = await self.__action_handler.create_budget_action(
                budget_id=budget.id,
                action_id=action_id
            )
            await self.__action_handler.handle_execution_status(
                action_id=action_id,
                entity_id=budget.id
            )
            return budget
        except CustomError as error:
            raise_exception(exception=error)

    async def create_budget(
        self,
        budget_body: CreateBudget,
        user_id: int,
        action_description: str
    ) -> Budget:
        try:
            action_id = await self.__action_handler.handle_action(
                user_id=user_id,
                action_description=action_description,
                action_type=ActionType.CREATE
            )
            budget = await self.__dao.create_budget(
                balance=budget_body.balance,
                year=budget_body.year
            )
            budget_action_id = await self.__action_handler.create_budget_action(
                budget_id=budget.id,
                action_id=action_id
            )
            await self.__action_handler.handle_execution_status(
                action_id=action_id,
                entity_id=budget.id
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
            action_id = await self.__action_handler.handle_action(
                user_id=user_id,
                action_description=action_description,
                action_type=ActionType.DELETE
            )
            budget = await self.__dao.delete_budget_by_id(
                budget_id=budget_id
            )
            budget_action_id = await self.__action_handler.create_budget_action(
                budget_id=budget.id,
                action_id=action_id
            )
            await self.__action_handler.handle_execution_status(
                action_id=action_id,
                entity_id=budget.id
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
            action_id = await self.__action_handler.handle_action(
                user_id=user_id,
                action_description=action_description,
                action_type=ActionType.DELETE
            )
            budget = await self.__dao.delete_budget_by_year(
                year=year
            )
            budget_action_id = await self.__action_handler.create_budget_action(
                budget_id=budget.id,
                action_id=action_id
            )
            await self.__action_handler.handle_execution_status(
                action_id=action_id,
                entity_id=budget.id
            )
            return budget
        except CustomError as error:
            raise_exception(exception=error)
