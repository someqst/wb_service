from aiohttp import ClientSession
from src.schema.product import ProductInfo
from aiohttp.client_exceptions import ClientError
from pydantic import ValidationError


async def get_info(article: int):
    url = f"https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={article}"
    try:
        async with ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                data = await response.json()
                return ProductInfo.model_validate(data)
    except (ClientError, ValidationError):
        return None
