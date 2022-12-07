from functools import partial

from fastapi import FastAPI

from apis.rest_api.api_v1.routers import api_router
from config import settings
from db.session import setup_db

app = FastAPI(
    debug=settings.DEBUG,
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description=settings.PROJECT_DESCRIPTION,
)


async def startup(app: FastAPI) -> None:
    app.state.settings = settings
    app.state.db_engine = await setup_db(settings)


async def shutdown(app: FastAPI) -> None:
    await app.state.db_engine.dispose()


app.add_event_handler(event_type="startup", func=partial(startup, app=app))
app.add_event_handler(event_type="shutdown", func=partial(shutdown, app=app))

app.include_router(api_router)

