import os
import datetime as dt
from pathlib import Path


ACCESS_TOKEN_EXPIRE_TIME = dt.timedelta(days=7)
ALGORITHM = "HS256"
# JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']   # should be kept secret
# JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']
JWT_SECRET_KEY = "iosjfojsdfjsojdefe"
JWT_REFRESH_SECRET_KEY = "jdjs0jw0ew303ke"


TORTOISE_ORM = {
    "connections": {"default": f'sqlite://{Path(__name__).parent}/db.sqlite3'},
    "apps": {
        "models": {
            "models": ['models',
                       'aerich.models',
                       ],
            "default_connection": "default",
        },
    },
}
