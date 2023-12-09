import csv
from fastapi import APIRouter, Depends, Query, UploadFile
from dependency_injector.wiring import inject, Provide
from starlette.responses import StreamingResponse
from src.budget.container import BudgetContainer

from src.budget.handler import BudgetImportHandler



budget_router = APIRouter()


@budget_router.post("/budget/import")
@inject
async def import_budget(
    file: UploadFile,
    handler: BudgetImportHandler = Depends(Provide[BudgetContainer.handler])
) -> None:
    contents = await file.read()
    return await handler.import_budget(
        contents=contents.decode().splitlines()
    )


@budget_router.get("/budget/export")
@inject
async def export_budget(
    balance_min: float = Query(None),
    balance_max: float = Query(None),
    year_min: int = Query(None),
    year_max: int = Query(None),
    handler: BudgetImportHandler = Depends(Provide[BudgetContainer.handler])
) -> StreamingResponse:
    return await handler.export_budget(
        balance_min=balance_min,
        balance_max=balance_max,
        year_min=year_min,
        year_max=year_max
    )
