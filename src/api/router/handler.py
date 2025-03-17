from fastapi import APIRouter
from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPBearer
from src.schema.product import ProductInfo
from src.api.router.auth import authenticate
from src.util.load_info import get_info
from src.service.product import ProductService
from src.api.dependencies import get_product_service


router = APIRouter()
security = HTTPBearer()


@router.get(
    "/{article}",
    response_model=ProductInfo,
    summary="Запуск периодического сбора данных",
)
async def add_product_to_schedule(
    article: int,
    product_service: ProductService = Depends(get_product_service),
    credentials: str = Depends(authenticate),
):
    product_info = await get_info(article)
    if product_info:
        name = product_info.data.products[0].name
        price = product_info.data.products[0].salePriceU
        rating = product_info.data.products[0].rating
        total_quantity = product_info.data.products[0].totalQuantity
        await product_service.update_product(
            article, name, price, rating, total_quantity, True
        )
        return product_info

    raise HTTPException(404, "No product found")


@router.post("/", response_model=ProductInfo, summary="Сбор данных в базу по артикулу")
async def load_info_to_bd(
    article: int,
    product_service: ProductService = Depends(get_product_service),
    credentials: str = Depends(authenticate),
):
    product_info = await get_info(article)
    if product_info:
        name = product_info.data.products[0].name
        price = product_info.data.products[0].salePriceU
        rating = product_info.data.products[0].rating
        total_quantity = product_info.data.products[0].totalQuantity
        await product_service.create_product(
            article, name, price, rating, total_quantity
        )
        return product_info

    raise HTTPException(status_code=404, detail="No product found")
