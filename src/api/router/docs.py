from fastapi import APIRouter
from fastapi.responses import RedirectResponse


router = APIRouter()


@router.get('/', response_class=RedirectResponse)
async def redirect_to_docs():
    return '/docs'
