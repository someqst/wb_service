from loguru import logger
from datetime import datetime
from pytz import timezone
from src.core.config import settings


logger.add(
    f"log/{datetime.now(timezone('Europe/Moscow')).strftime('%d-%m-%Y')}.log",
    format="{time} {level} {message}\n",
    rotation="500MB",
    level=settings.LOGGING_LEVEL,
    enqueue=True,
)
