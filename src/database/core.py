from database.models import Product, ScheduleProduct
from sqlalchemy import select, update, delete, insert
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from data.config import settings


engine = create_async_engine(settings.DB_URI.get_secret_value())
async_session_maker = async_sessionmaker(engine)


def connection(func):
    async def wrapper(*args, **kwargs):
        async with async_session_maker() as session:
            try:
                return await func(*args, **kwargs, session=session)
            except Exception as e:
                await session.rollback()
                raise e
            finally:
                await session.close()
    return wrapper



class DataBase:

    @classmethod
    @connection
    async def write_product(cls, article, name, price, rating, total_quantity, session: AsyncSession = None):
        product = Product(article = article, name = name, price = price, rating = rating, total_quantity = total_quantity)
        await session.merge(product)
        await session.commit()


    @classmethod
    @connection
    async def write_product_schedule(cls, article, name, price, rating, total_quantity, session: AsyncSession = None):
        await cls.write_product(article, name, price, rating, total_quantity)
        product = ScheduleProduct(article = article)
        await session.merge(product)
        await session.commit()


    @classmethod
    @connection
    async def select_scheduled_products(cls, session: AsyncSession = None):
        return (await session.execute(select(ScheduleProduct))).scalars().all()
    

    @classmethod
    @connection
    async def select_product_info(cls, article, session: AsyncSession = None) -> Product:
        return (await session.execute(select(Product).where(Product.article == article))).scalar_one_or_none() 
