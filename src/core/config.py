from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal
from pathlib import Path


BASE_PATH = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    DB_URI: SecretStr
    LOGGING_LEVEL: Literal["INFO", "DEBUG", "WARNING"] = "INFO"
    HTTPBEARER: SecretStr
    BOT_TOKEN: SecretStr

    model_config = SettingsConfigDict(
        env_file=BASE_PATH / ".env", env_file_encoding="utf-8"
    )


settings = Settings()
