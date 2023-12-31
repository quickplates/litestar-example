from pydantic import BaseSettings, Extra
from pydantic.env_settings import SettingsSourceCallable


class BaseConfig(BaseSettings):
    """Base configuration class."""

    class Config:
        """Pydantic configuration."""

        # Environment variables prefix
        env_prefix = "LITESTAR_EXAMPLE_"
        # Delimiter for nested models in environment variables
        env_nested_delimiter = "__"
        # Use dotenv file if present
        env_file = ".env"
        # Don't raise errors for extra fields
        extra = Extra.allow

        @classmethod
        def customise_sources(
            cls,
            init_settings: SettingsSourceCallable,
            env_settings: SettingsSourceCallable,
            file_secret_settings: SettingsSourceCallable,
        ) -> tuple[SettingsSourceCallable, ...]:
            # Define the order of settings sources
            return env_settings, init_settings, file_secret_settings
