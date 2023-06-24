from litestar_example.config.base import BaseConfig


class Config(BaseConfig):
    """Configuration for the application."""

    foo: str = "bar"
