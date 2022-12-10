from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise
from routers import user, todo
from dependencies import get_user
import config


app = FastAPI()

register_tortoise(
    app,
    config=config.TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get('/')
async def root():
    return {"a": [1, 2, 3]}


app.include_router(
    user.router,
    prefix='/user',
    dependencies=[]
)

app.include_router(
    todo.router,
    prefix='/tasks',
    dependencies=[]
)