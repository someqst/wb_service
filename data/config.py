from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    DB_URI: SecretStr
    POSTGRES_USER: SecretStr
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_DB: SecretStr
    
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )

settings = Settings()