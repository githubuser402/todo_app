from fastapi import APIRouter, Depends, status, Body
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.exceptions import HTTPException
from models import User, UserInPydantic, UserPydantic
from dependencies import get_user
from utils.logger import logger
from pydantic import BaseModel
from typing import List, Union
from utils.token import Token as TokenGenerator
from tortoise.exceptions import IntegrityError

router = APIRouter()


class Token(BaseModel):
    token: str
    token_type: str


class Exception(BaseModel):
    status_code: int
    detail: str


@router.post('/token', response_model=Union[Token, Exception])
async def refresh_token(form_data: OAuth2PasswordRequestForm = Depends()):
    logger.debug(f"{form_data.username} {form_data.password}")
    user = await User.filter(username=form_data.username).first()
    logger.debug(user)

    if not user.verify_hash(form_data.password):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='Wrong password')

    token = TokenGenerator.encode(user.id)
    return {'token': token, 'token_type': 'bars'}


@router.post('/register', response_model=Union[Token, Exception])
async def create_user(user_data: UserInPydantic = Body()):
    try:
        user = User()
        user.username = user_data.username
        user.password = User.generate_hash(user_data.password)
        user.email = user_data.email
        await user.save()

        token = TokenGenerator.encode(user.id)
        return {'token': token, 'token_type': 'bars'}
    except IntegrityError:
        return {'status_code': status.HTTP_409_CONFLICT, 'detail': f'User named {user_data.username} already exists'}


@router.get('/info', response_model=Union[UserPydantic, Exception])
async def get_users(user: User = Depends(get_user)):
    return await UserPydantic.from_tortoise_orm(user)
