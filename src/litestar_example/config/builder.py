from pydantic import ValidationError

from litestar_example.config.errors import ConfigError
from litestar_example.config.models import Config


class ConfigBuilder:
    """Builds the config."""

    def build(self) -> Config:
        """Build the config."""

        try:
            return Config()
        except ValidationError as ex:
            raise ConfigError from ex
