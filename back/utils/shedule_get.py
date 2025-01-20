from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loader import db
from back.utils.load_info import get_info 


async def schedule_parse():
    print('start')
    products = await db.select_scheduled_products()
    if products:
        for product in products:
            product_info = await get_info(product.article)
            if product_info:
                await db.write_product(product.article, product_info.data.products[0].name,product_info.data.products[0].salePriceU,
                                       product_info.data.products[0].rating, product_info.data.products[0].totalQuantity)
            else:
                pass
    else:
        pass


scheduler = AsyncIOScheduler()
scheduler.add_job(schedule_parse, 'cron', minute='0,16')