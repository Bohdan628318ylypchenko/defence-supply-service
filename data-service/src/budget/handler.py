import csv
from io import StringIO
from fastapi.responses import StreamingResponse
from pydantic.error_wrappers import ValidationError
from src.budget.models import Budget, FullBudgetModel
from .dao import BudgetImportDAO
from src.utils.error_handler import raise_exception
from src.errors import exceptions


class BudgetImportHandler:

    def __init__(
        self,
        dao: BudgetImportDAO
    ) -> None:
        self.__dao = dao


    async def import_budget(
        self,
        contents: list[str]
    ) -> None:
        try:
            budget_list = await self.__parse_to_list(contents=contents)
            await self.__dao.import_budget(
                budget_list=budget_list
            )
        except exceptions.CustomError as error:
            raise_exception(exception=error)

    async def __validate_header(self, header) -> bool:
        if len(header) != 2:
            return False
        if "balance" not in header or "year" not in header:
            return False
        return True

    async def __parse_to_list(self, contents: list[str]) -> list[Budget]:
        try:
            header = contents.pop(0)
            header = header.split(",")
            if not await self.__validate_header(header):
                raise exceptions.InvalidBudgetImportHeader
            budget_items = [tuple(map(lambda x: x, item.split(','))) for item in contents]
            budget_models = [Budget(**dict(zip(header, item))) for item in budget_items] # type: ignore
            return budget_models
        except ValidationError:
            raise exceptions.InvalidBudgetImportBody
        
    async def export_budget(
        self,
        balance_min: float | None,
        balance_max: float | None,
        year_min: float | None,
        year_max: float | None
    ) -> StreamingResponse:
        budgets = await self.__dao.export_budget(
            balance_min=balance_min,
            balance_max=balance_max,
            year_min=year_min,
            year_max=year_max
        )
        return await self.__create_csv(
            budgets=budgets
        )

    async def __create_csv(
        self,
        budgets: list[FullBudgetModel]
    ) -> StreamingResponse:
        csv_buffer = StringIO()
        csv_writer = csv.writer(csv_buffer)

        header = ["id", "is_active", "year", "balance"]
        csv_writer.writerow(header)

        for budget in budgets:
            row = [budget.id, budget.is_active, budget.year, budget.balance] 
            csv_writer.writerow(row)

        csv_content = csv_buffer.getvalue()

        csv_buffer.close()
        return StreamingResponse(iter([csv_content]), media_type="text/csv", headers={"Content-Disposition": "attachment; filename=budgets.csv"})
