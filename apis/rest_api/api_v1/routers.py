from typing import Any
from fastapi.responses import HTMLResponse
from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("")
async def get_views(response_class=HTMLResponse) -> Any:
    return ''
