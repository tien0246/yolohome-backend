import jwt
from datetime import datetime, timedelta
from app.utils.config import config

def create_access_token(data):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(seconds=config.jwt_expire)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, config.jwt_secret, algorithm=config.jwt_algorithm)

def decode_access_token(token):
    return jwt.decode(token, config.jwt_secret, algorithms=[config.jwt_algorithm])
