from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
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

origins = [
    '*',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],    
)


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