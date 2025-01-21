from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from data.config import settings


security = HTTPBearer()


async def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != settings.HTTPBEARER.get_secret_value():
        raise HTTPException(status_code=401, detail='Invalid username or password')
    return credentials.credentials