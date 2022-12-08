from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise
from routers import user
from dependencies import get_user
import config.database


app = FastAPI()

register_tortoise(
    app,
    db_url=config.database.DATABASE_URL,
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get('/')
async def root():
    return {"a": [1,2,3]}


app.include_router(
    user.router,
    prefix="/users",
    dependencies=[]
)
