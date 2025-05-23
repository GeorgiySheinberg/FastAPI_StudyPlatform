from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from study_platform.backend.api import router as api_router
from study_platform.backend.core.config import settings
from study_platform.backend.core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()




app = FastAPI(
    lifespan=lifespan
)
app.include_router(
    api_router, prefix=settings.api.api_prefix,
)


if __name__ == "__main__":
    uvicorn.run(
        "study_platform.backend.main:app",
            host=settings.run.host,
            port=settings.run.port,
            reload=True,
    )
