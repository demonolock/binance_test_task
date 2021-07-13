from pydantic import BaseSettings, Field


class Settings(BaseSettings):

    windows_size: int = Field(..., env="WINDOW_SIZE")
    subscribed_symbols: str = Field(..., env="SUBSCRIBED_SYMBOLS")
    frequency: str = Field(..., env="FREQUENCY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()