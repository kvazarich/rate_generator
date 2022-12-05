from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from sqlalchemy.orm import sessionmaker

from config import settings

session_maker = sessionmaker(expire_on_commit=False, class_=AsyncSession)


async def setup_db(app: FastAPI) -> AsyncEngine:
    engine = create_async_engine(
        app.state.settings.POSTGRES_URI,
        echo=True,
        future=True,
        pool_size=settings.MAX_PG_CONNECTIONS
    )
    session_maker.configure(bind=engine)
    return engine


async def get_session_maker():
    return session_maker
