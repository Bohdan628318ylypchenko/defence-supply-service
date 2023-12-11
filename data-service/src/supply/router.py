from fastapi import APIRouter, Depends, Query, UploadFile
from dependency_injector.wiring import inject, Provide
from fastapi.responses import StreamingResponse
from .handler import SupplyHandler
from .container import SupplyContainer


supply_router = APIRouter()


@supply_router.post("/supply/import")
@inject
async def import_supply(
    file: UploadFile,
    handler: SupplyHandler = Depends(Provide[SupplyContainer.handler])
) -> None:
    contents = await file.read()
    return await handler.import_supply(
        contents=contents.decode().splitlines()
    )


@supply_router.get("/supply/export")
@inject
async def export_supply(
    unit_cost_min: float = Query(None),
    unit_cost_max: float = Query(None),
    unit_type: str = Query(None),
    norm_unit_count_day_min: float = Query(None),
    norm_unit_count_day_max: float = Query(None),
    handler: SupplyHandler = Depends(Provide[SupplyContainer.handler])
) -> StreamingResponse:
    return await handler.export_supply(
        unit_cost_min=unit_cost_min,
        unit_cost_max=unit_cost_max,
        unit_type=unit_type,
        norm_unit_count_day_min=norm_unit_count_day_min,
        norm_unit_count_day_max=norm_unit_count_day_max
    )

