from datetime import date
from fastapi import APIRouter, Depends, Query, UploadFile
from dependency_injector.wiring import inject, Provide
from fastapi.responses import StreamingResponse
from .container import AvailabilityContainer
from .handler import AvailabilityHandler


availability_router = APIRouter()


@availability_router.post("/availability/import")
@inject
async def import_availability(
    file: UploadFile,
    handler: AvailabilityHandler = Depends(Provide[AvailabilityContainer.handler])
) -> None:
    contents = await file.read()
    return await handler.import_availability(
        contents=contents.decode().splitlines()
    )


@availability_router.get("/availability/export")
@inject
async def export_availability(
    start_date: date = Query(None),
    end_date: date = Query(None),
    supply_id: int = Query(None),
    handler: AvailabilityHandler = Depends(Provide[AvailabilityContainer.handler])
) -> StreamingResponse:
    return await handler.export_availability(
        start_date=start_date,
        end_date=end_date,
        supply_id=supply_id
    )
