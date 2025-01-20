import asyncio
from fastapi import FastAPI, Depends
from loader import db, dp, bot
from back.utils.load_info import get_info
from fastapi.exceptions import HTTPException
from data.schemes import ProductsPOST, ProductInfo
from typing import Annotated
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from back.utils.shedule_get import scheduler
from uvicorn import Config, Server


app = FastAPI()
security = HTTPBearer()


@app.post('/api/v1/products', response_model=ProductInfo, summary='Сбор данных в базу по артикулу')
async def load_info_to_bd(product: ProductsPOST, credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]):
    print(credentials.credentials)
    if credentials.credentials != 'verystrongauthxd':
        raise HTTPException(401, 'Invalid username or password')    

    product_info = await get_info(product.articul)
    if product_info:
        name = product_info.data.products[0].name
        price = product_info.data.products[0].salePriceU
        rating = product_info.data.products[0].rating
        total_quantity = product_info.data.products[0].totalQuantity
        await db.write_product(product.articul, name, price, rating, total_quantity)
        return product_info
    else:
        raise HTTPException(403, 'No product found')


@app.get('/api/v1/subscribe/{artikul}', response_model=ProductInfo, summary='Запуск периодического сбора данных')
async def load_info_to_bd(artikul: int, credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]):
    if credentials.credentials != 'verystrongauthxd':
        raise HTTPException(401, 'Invalid username or password')   

    product_info = await get_info(artikul)
    if product_info:
        name = product_info.data.products[0].name
        price = product_info.data.products[0].salePriceU
        rating = product_info.data.products[0].rating
        total_quantity = product_info.data.products[0].totalQuantity
        await db.write_product_schedule(artikul, name, price, rating, total_quantity)
        return product_info
    else:
        raise HTTPException(403, 'No product found')
    
async def main():
    scheduler.start()
    print("Scheduler started")

    server = Server(Config(app=app, host='0.0.0.0', port=8002))
    await server.serve()

    scheduler.shutdown()
    print("Scheduler shutdown")

if __name__ == '__main__':
    asyncio.run(main())