import os
import datetime as dt

ACCESS_TOKEN_EXPIRE_TIME = dt.timedelta(minutes=5)  # 30 minutes
# REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
# JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']   # should be kept secret
# JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']   
JWT_SECRET_KEY = "iosjfojsdfjsojdefe"
JWT_REFRESH_SECRET_KEY = "jdjs0jw0ew303ke"
