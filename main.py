from fastapi import FastAPI
from contextlib import asynccontextmanager

# from pydantic import EmailStr, BaseModel
from items_views import router as items_router
from users.views import router as users_router
from core.models import Base, db_helper
from core.config import settings
from api_v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_router)
app.include_router(router_v1, prefix=settings.api_v1_prefix)


@app.get(
    "/",
    summary="Вернуть приветствие",
)
def hello_index():
    return {"Message": "Hello World!!!"}


@app.get("/hello/")
def hello(name: str):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


# @app.post("/calc/add/")
# def add(a: int, b: int):
#     return {
#         "a": a,
#         "b": b,
#         "result": a + b,
#     }
