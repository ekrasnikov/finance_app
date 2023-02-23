import uvicorn
from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette_context.middleware import RawContextMiddleware

import application

from configs.api import config
from app.v1 import router as api_router_v1

middleware = [Middleware(RawContextMiddleware)]

app = FastAPI(
    title="Finance App",
    version=config.version,
    docs_url="/docs/api",
    redoc_url="/redoc/api",
    openapi_url="/docs/api/openapi.json",
    middleware=middleware,
)
app.include_router(api_router_v1, prefix='/api/v1')


@app.on_event("startup")
async def on_startup() -> None:
    await application.on_startup()


@app.on_event("shutdown")
async def on_shutdown() -> None:
    await application.on_shutdown()


if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        forwarded_allow_ips="*",
    )
