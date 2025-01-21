from pydantic import BaseModel
from typing import List


class ProductsPOST(BaseModel):
    articul: int



class Product(BaseModel):
    name: str
    salePriceU: int
    rating: int
    totalQuantity: int


class Data(BaseModel):
    products: List[Product]


class ProductInfo(BaseModel):
    data: Data

