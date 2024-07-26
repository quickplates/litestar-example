from pydantic import BaseModel, Field

from litestar_example.config.base import BaseConfig


class ServerConfig(BaseModel):
    """Configuration for the server."""

    host: str = Field(
        "0.0.0.0",
        title="Host",
        description="Host to run the server on.",
    )
    port: int = Field(
        8080,
        ge=0,
        le=65535,
        title="Port",
        description="Port to run the server on.",
    )
    trusted: str | list[str] | None = Field(
        "*",
        title="Trusted",
        description="Trusted IP addresses.",
    )


class Config(BaseConfig):
    """Configuration for the application."""

    server: ServerConfig = Field(
        ServerConfig(),
        title="Server",
        description="Configuration for the server.",
    )
