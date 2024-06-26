from pydantic_settings import BaseSettings
import json


class RSSSourceSettings(BaseSettings):
    feed_url: str


class DataSourceSettings(BaseSettings):
    rss: list[RSSSourceSettings] | None = None


class OpenAISettings(BaseSettings):
    api_key: str
    llm: str = "gpt-4o"


class Settings(BaseSettings):
    open_ai: OpenAISettings
    data_sources: DataSourceSettings

    class Config:
        env_prefix = "AI_PODCAST_GENERATOR_"  # Prefix for environment variables
        env_nested_delimiter = "__"


def load_settings_from_json(file_path: str) -> Settings:
    with open(file_path, "r") as file:
        data = json.load(file)

    settings = Settings(**data)

    return settings
