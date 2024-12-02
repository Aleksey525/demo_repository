from pydantic import BaseModel, Field, ValidationError, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class RedisSettings(BaseModel):
    host: str
    port: int
    password: Optional[str] = Field(default=None)

    @field_validator('port')
    def validate_port(cls, v):
        if not 0 <= v <= 65535:
            raise ValueError('Порт должен быть в диапазоне от 0 до 65535')
        return v


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env_test',
        extra='ignore',
        env_nested_delimiter='__'
    )
    redis: RedisSettings
    optional_settings: Optional[str] = Field(default=None)


try:
    settings = Settings()
    print(settings.model_dump())
except ValidationError as e:
    print(f'Ошибки валидации: {e}')
