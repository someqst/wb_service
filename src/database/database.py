from src.core.config import settings

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import AsyncGenerator


engine = create_async_engine(settings.DB_URI.get_secret_value())
LocalSession = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db() -> AsyncGenerator:
    async with LocalSession() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()
