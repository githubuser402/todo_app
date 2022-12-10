from fastapi import Header, HTTPException, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from utils.token import Token
from utils.logger import logger
from models import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/token", scheme_name="JWT")


async def get_user(token: str = Depends(oauth2_scheme)):
    logger.debug(token)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        token_data = Token.decode(token)
        # token_data = {"id": 1}
    except Exception as ex:
        raise credentials_exception

    user = await User.get(id=token_data['id'])
    
    if not user:
        raise credentials_exception
    
    logger.debug(user)
    return user 