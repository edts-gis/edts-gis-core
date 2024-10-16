from typing import Optional

from pydantic import computed_field, SecretStr
from pydantic_settings import BaseSettings
from sqlalchemy.engine.url import URL


class Config(BaseSettings):
    DB_DRIVER: str
    DB_HOSTNAME: str
    DB_USERNAME: str
    DB_PASSWORD: SecretStr
    DB_PORT: int
    DB_NAME: str
    CLOUD_SQL_INSTANCE_UNIX_SOCKET: Optional[str] = None

    @computed_field
    @property
    def DB_URI(self) -> URL:
        query = {
            "unix_sock": f"{self.CLOUD_SQL_INSTANCE_UNIX_SOCKET}/.s.PGSQL.{self.DB_PORT}"
        } if self.CLOUD_SQL_INSTANCE_UNIX_SOCKET else None
        db_uri = URL.create(
            drivername = self.DB_DRIVER,
            username = self.DB_USERNAME,
            password = self.DB_PASSWORD.get_secret_value(),
            host = self.DB_HOSTNAME,
            port = self.DB_PORT,
            database = self.DB_NAME,
            query = query
        )
        return db_uri