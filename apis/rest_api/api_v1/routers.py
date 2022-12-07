from typing import Any
from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("tickers/current")
async def get_current_rates() -> Any:
    return {}
