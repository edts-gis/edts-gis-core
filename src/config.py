from pydantic import computed_field, SecretStr
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DB_DRIVER: str
    DB_HOSTNAME: str
    DB_USERNAME: str
    DB_PASSWORD: SecretStr
    DB_PORT: int
    DB_NAME: str

    @computed_field
    @property
    def DB_URI(self) -> SecretStr:
        db_uri = SecretStr(
            "{driver}://{username}:{password}@{hostname}:{port}/{name}".format(
                driver = self.DB_DRIVER,
                hostname = self.DB_HOSTNAME,
                username = self.DB_USERNAME,
                password = self.DB_PASSWORD.get_secret_value(),
                port = self.DB_PORT,
                name = self.DB_NAME
            )
        )
        return db_uri