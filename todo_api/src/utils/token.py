from typing import Union, Any
import config
from jose import jwt, JWTError
import datetime as dt

class Token:
    @classmethod
    def encode(cls, user_id: int) -> str:
        token_data = {
            "id": user_id,
            "exp": dt.datetime.utcnow() + config.ACCESS_TOKEN_EXPIRE_TIME
        }

        return jwt.encode(token_data, config.JWT_SECRET_KEY, config.ALGORITHM)

    @classmethod
    def decode(cls, token: str) -> dict:
        try:
            return jwt.decode(token, config.JWT_SECRET_KEY, algorithms=[config.ALGORITHM,])
        except JWTError as ex:
            print(ex)
            raise ex
