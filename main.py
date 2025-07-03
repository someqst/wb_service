import uvicorn
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from contextlib import asynccontextmanager

from src.util.logging import logger
from src.api.router.handler import router as product_router
from src.api.router.docs import router as docs_router
from src.util.schedule_get import scheduler
from bot.main import dp, bot


@asynccontextmanager
async def lifespan(app):
    scheduler.start()
    task = asyncio.create_task(dp.start_polling(bot))
    yield
    task.cancel()
    scheduler.shutdown()


app = FastAPI(title="Wb Service", lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost", "127.0.0.1", "0.0.0.0"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def handle_exceptions_middleware(req: Request, ex: Exception):
    logger.error(f"{ex}\nEndpoint: {req.url}")

    raise HTTPException(status_code=500, detail="Internal Server Error")


app.include_router(docs_router)
app.include_router(product_router, prefix="/api/v1/product", tags=["product"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
