from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.database.models.product import Product
from src.schema.product import ProductFilter


class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, article, name, price, rating, total_quantity):
        product = Product(
            article=article,
            name=name,
            price=price,
            rating=rating,
            total_quantity=total_quantity,
        )
        await self.session.merge(product)
        await self.session.commit()

    async def update(
        self, article, name, price, rating, total_quantity, is_scheduled: bool = False
    ):
        product = Product(
            article=article,
            name=name,
            price=price,
            rating=rating,
            total_quantity=total_quantity,
            is_scheduled=is_scheduled,
        )
        await self.session.merge(product)
        await self.session.commit()

    async def get_products(self, filter: ProductFilter) -> List[Product] | None:
        return (
            (
                await self.session.execute(
                    select(Product).filter(Product.is_scheduled == filter.is_scheduled)
                )
            )
            .scalars()
            .all()
        )

    async def get_product(self, article) -> Product | None:
        return (
            await self.session.execute(
                select(Product).where(Product.article == article)
            )
        ).scalar_one_or_none()
