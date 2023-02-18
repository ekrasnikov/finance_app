from pydantic import BaseSettings


class Config(BaseSettings):
    version: str = "0.0.0"


config = Config()
