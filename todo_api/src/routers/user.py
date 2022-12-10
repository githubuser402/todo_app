from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.exceptions import HTTPException
from models import User, UserInPydantic, UserPydantic
from dependencies import get_user
from utils.logger import logger
from pydantic import BaseModel
from typing import List
from utils.token import Token as TokenGenerator

router = APIRouter()


class Token(BaseModel):
    token: str
    token_type: str


@router.post('/token')
async def create_token(form_data: OAuth2PasswordRequestForm = Depends()):
    logger.debug(f"{form_data.username} {form_data.password}")
    user = await User.filter(username=form_data.username).first()
    logger.debug(user)

    if user:
        token = TokenGenerator.encode(user.id)
        return {'token': token, 'token_type': 'Bearer'}
        
        
    user = User()
    user.username = form_data.username
    user.password = User.generate_hash(form_data.password)
    await user.save()
    
    token = TokenGenerator.encode(user.id)
    return {'token': token, 'token_type': 'bars'}


@router.get('/', response_model=List[UserPydantic])
async def get_users(user: User = Depends(get_user)):
    print(type(user))
    users = await UserPydantic.from_queryset(User.all())
    logger.debug(users)
    return users
