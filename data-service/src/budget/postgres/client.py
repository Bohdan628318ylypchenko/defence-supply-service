from loguru import logger
from asyncpg.exceptions import UniqueViolationError
from databases import Database
from src.budget.models import Budget, FullBudgetModel
from src.errors import exceptions
from . import queries


class BudgetImportClient:

    def __init__(
        self,
        db: Database
    ) -> None:
        self.__db = db

    async def import_budget(
        self,
        budget_list: list[Budget]
    ) -> None:
        try:
            logger.debug("BudgetClient started importing budgets")
            await self.__db.execute_many(
                query=queries.IMPORT_BUDGET,
                values=[item.dict() for item in budget_list]
            )
            logger.debug("BudgetClient finished importing budgets")
        except UniqueViolationError:
            raise exceptions.BudgetYearUniqueViolation
         
    async def export_budget(
        self,
        balance_min: float | None,
        balance_max: float | None,
        year_min: float | None,
        year_max: float | None
    ) -> list[FullBudgetModel]:
        logger.debug("BudgetClient started exporting budgets")
        values = {
            "balance_min": balance_min,
            "balance_max": balance_max,
            "year_min": year_min,
            "year_max": year_max
        }
        budgets_raw = await self.__db.fetch_all(
            query=queries.EXPORT_BUDGET,
            values = values
        )
        return [FullBudgetModel.parse_obj(budget) for budget in budgets_raw]
