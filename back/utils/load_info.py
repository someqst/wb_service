from aiohttp import ClientSession
from data.schemes import ProductInfo


async def get_info(article: int):
    async with ClientSession() as session:
        try:
            async with session.get(f'https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={article}') as response:
                if response.status == 200:
                    response = await response.json()
                    try:
                        return ProductInfo.model_validate(response)
                    except:
                        return None
                else:
                    return None
        except:
            return None