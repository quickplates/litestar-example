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
    concurrency: int | None = Field(
        None,
        ge=1,
        title="Concurrency",
        description="Number of concurrent requests to handle.",
    )
    backlog: int = Field(
        2048,
        ge=0,
        title="Backlog",
        description="Number of requests to queue.",
    )
    keepalive: int = Field(
        5,
        ge=0,
        title="Keepalive",
        description="Number of seconds to keep connections alive.",
    )


class Config(BaseConfig):
    """Configuration for the application."""

    server: ServerConfig = Field(
        ServerConfig(),
        title="Server",
        description="Configuration for the server.",
    )
