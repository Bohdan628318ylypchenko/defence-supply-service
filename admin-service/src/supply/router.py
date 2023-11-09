from fastapi import APIRouter


supply_router = APIRouter()


@supply_router.get("/hello")
async def get_hello() -> dict:
    return {"message": "hello"}
