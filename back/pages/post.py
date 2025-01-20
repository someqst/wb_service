from fastapi import APIRouter
from fastapi import Depends
from loader import db
from back.utils.load_info import get_info
from fastapi.exceptions import HTTPException
from data.schemes import ProductsPOST, ProductInfo
from data.schemes import ProductInfo
from typing import Annotated
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


router = APIRouter()
security = HTTPBearer()


@router.post('/', response_model=ProductInfo, summary='Сбор данных в базу по артикулу')
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
