from pydantic import BaseSettings, PostgresDsn, Field


class Config(BaseSettings):
    version: str = "0.0.0"
    postgres_dsn: PostgresDsn = Field('postgresql://postgres@localhost/postgres')


config = Config()
