from src.schema.product import Product, ProductFilter
from src.database.repositories.product import ProductRepository


class ProductService:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    async def create_product(self, article, name, price, rating, total_quantity):
        await self.product_repo.create(
            article, name, price, rating, total_quantity
        )


    async def update_product(
        self, article, name, price, rating, total_quantity, is_scheduled: bool = False
    ):
        await self.product_repo.update(
            article, name, price, rating, total_quantity, is_scheduled
        )

    async def get_products(self, filter: ProductFilter):
        return await self.product_repo.get_products(filter)

    async def get_product(self, article: int):
        return await self.product_repo.get_product(article)
