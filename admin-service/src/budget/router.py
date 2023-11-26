from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from src.budget.container import BudgetContainer
from src.budget.handler import BudgetHandler
from src.budget.models import Budget, CreateBudget


budget_router = APIRouter()


@budget_router.get("/budget/{budget_id}")
@inject
async def get_budget_by_id(
    budget_id: int,
    user_id: int,
    action_description: str,
    handler: BudgetHandler = Depends(Provide[BudgetContainer.handler])
) -> Budget:
    return await handler.get_budget_by_id(
        budget_id=budget_id,
        user_id=user_id,
        action_description=action_description
    )


@budget_router.get("/budget")
@inject
async def get_budget_by_year(
    year: int,
    user_id: int,
    action_description: str,
    handler: BudgetHandler = Depends(Provide[BudgetContainer.handler])
) -> Budget:
    return await handler.get_budget_by_year(
        year=year,
        user_id=user_id,
        action_description=action_description
    )


@budget_router.post("/budget")
@inject
async def create_budget(
    budget_body: CreateBudget,
    user_id: int,
    action_description: str,
    handler: BudgetHandler = Depends(Provide[BudgetContainer.handler])
) -> Budget:
    return await handler.create_budget(
        budget_body=budget_body,
        user_id=user_id,
        action_description=action_description
    )


@budget_router.delete("/budget/{budget_id}")
@inject
async def delete_budget_by_id(
    budget_id: int,
    user_id: int,
    action_description: str,
    handler: BudgetHandler = Depends(Provide[BudgetContainer.handler])
) -> Budget:
    return await handler.delete_budget_by_id(
        budget_id=budget_id,
        user_id=user_id,
        action_description=action_description
    )


@budget_router.delete("/budget")
@inject
async def delete_budget_by_year(
    year: int,
    user_id: int,
    action_description: str,
    handler: BudgetHandler = Depends(Provide[BudgetContainer.handler])
) -> Budget:
    return await handler.delete_budget_by_year(
        year=year,
        user_id=user_id,
        action_description=action_description
    )
