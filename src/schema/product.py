from typing import List
from pydantic import BaseModel, ConfigDict
from typing import ClassVar


class Product(BaseModel):
    name: str
    salePriceU: int
    rating: int
    totalQuantity: int
    model_config: ClassVar[dict] = ConfigDict(from_attributes=True, extra="ignore")


class Data(BaseModel):
    products: List[Product]


class ProductInfo(BaseModel):
    data: Data


class ProductFilter(BaseModel):
    is_scheduled: bool = False
