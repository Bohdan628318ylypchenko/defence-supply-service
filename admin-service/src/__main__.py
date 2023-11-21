from collections.abc import Callable
import uvicorn  # type: ignore
from fastapi import (
    Request,
    Response,
)
from loguru import logger
from .container import Application
from src.supply.router import supply_router
from src.availability.router import availability_router
from src.budget.router import budget_router

application_container = Application()
fastapi_app = application_container.fastapi_app()


@fastapi_app.middleware("http")
async def log_middle(request: Request, call_next: Callable) -> Response:
    url = "/" + str(request.url).removeprefix(str(request.base_url))
    logger.info(f"Request: {request.method} {url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code} {url}")
    return response


fastapi_app.include_router(
    supply_router,
    tags=["supply"]
)
fastapi_app.include_router(
    availability_router,
    tags=["availability"]
)
fastapi_app.include_router(
    budget_router,
    tags=["budget"]
)


def run() -> None:
    uvicorn.run(
        "src.__main__:fastapi_app",
        host=application_container.config.service.host(), # type: ignore
        port=application_container.config.service.port(),  # type: ignore
        loop="uvloop",
    )
