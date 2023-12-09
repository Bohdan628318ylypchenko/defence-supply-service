from .postgres.client import BudgetImportClient
from .models import Budget, FullBudgetModel


class BudgetImportDAO:

    def __init__(
        self,
        db_client: BudgetImportClient
    ) -> None:
        self.__db_client = db_client

    async def import_budget(
        self,
        budget_list: list[Budget]
    ) -> None:
        await self.__db_client.import_budget(
            budget_list=budget_list
        )

    async def export_budget(
        self,
        balance_min: float | None,
        balance_max: float | None,
        year_min: float | None,
        year_max: float | None
    ) -> list[FullBudgetModel]:
        return await self.__db_client.export_budget(
            balance_min=balance_min,
            balance_max=balance_max,
            year_min=year_min,
            year_max=year_max
        )
