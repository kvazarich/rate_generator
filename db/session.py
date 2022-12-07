from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from sqlalchemy.orm import sessionmaker


session_maker = sessionmaker(expire_on_commit=False, class_=AsyncSession)


async def setup_db(settings) -> AsyncEngine:
    engine = create_async_engine(
        settings.POSTGRES_URI,
        echo=True,
        future=True,
    )
    session_maker.configure(bind=engine)
    return engine


async def get_session_maker():
    return session_maker
