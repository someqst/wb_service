import asyncio, sys, os
from fastapi import FastAPI
from back.utils.shedule_get import scheduler
from uvicorn import Config, Server
from back.pages.get import router as get_router
from back.pages.post import router as post_router



app = FastAPI()
    

app.include_router(post_router, prefix='/api/v1/products', tags=['POST'])
app.include_router(get_router, prefix='/api/v1/subscribe', tags=['GET'])

async def main():
    scheduler.start()

    server = Server(Config(app=app, host='0.0.0.0', port=8002))
    await server.serve()

    scheduler.shutdown()

if __name__ == '__main__':
    asyncio.run(main())