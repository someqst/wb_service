from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.core.config import settings


security = HTTPBearer()


async def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != settings.HTTPBEARER.get_secret_value():
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return credentials.credentials
