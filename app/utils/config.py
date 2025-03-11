import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Config(BaseSettings):
    db_host: str = os.getenv("DB_HOST")
    db_port: int = int(os.getenv("DB_PORT"))
    db_user: str = os.getenv("DB_USER")
    db_password: str = os.getenv("DB_PASSWORD")
    db_name: str = os.getenv("DB_NAME")
    aio_username: str = os.getenv("AIO_USERNAME")
    aio_key: str = os.getenv("AIO_KEY")
    jwt_secret: str = os.getenv("JWT_SECRET")
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM")
    jwt_expire: int = int(os.getenv("JWT_EXPIRE"))
    rabbitmq_url: str = os.getenv("RABBITMQ_URL")
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

config = Config()
