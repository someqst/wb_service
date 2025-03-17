from fastapi import Depends
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.util.load_info import get_info
from src.schema.product import ProductFilter
from src.service.product import ProductService
from src.api.dependencies import get_product_service


async def schedule_parse(
    product_service: ProductService = Depends(get_product_service),
):
    products = await product_service.get_products(ProductFilter(is_scheduled=True))

    if products:
        for product in products:
            product_info = await get_info(product.article)
            if product_info:
                await product_service.update_product(
                    product.article,
                    product_info.data.products[0].name,
                    product_info.data.products[0].salePriceU,
                    product_info.data.products[0].rating,
                    product_info.data.products[0].totalQuantity,
                )
    return


scheduler = AsyncIOScheduler()
scheduler.add_job(schedule_parse, "cron", minute="30")
