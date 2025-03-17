from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.database import get_db
from src.service.product import ProductService
from src.database.repositories.product import ProductRepository


def get_product_service(session: AsyncSession = Depends(get_db)):
    return ProductService(ProductRepository(session))
