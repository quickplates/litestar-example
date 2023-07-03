from typing import Literal, TypeVar

from pydantic import BaseModel, Field, validator

from litestar_example.config.base import BaseConfig

T = TypeVar("T")


def _split_string(v: T, sep: str = ",") -> T | list[str]:
    """If the value is a string, split it by the separator."""

    if isinstance(v, str):
        return v.split(sep)
    return v


def _split_string_validator(*args, sep: str = ",", **kwargs):
    """Create a validator that splits values by a separator if they are strings."""

    def fn(value):
        return _split_string(value, sep=sep)

    return validator(*args, pre=True, allow_reuse=True, **kwargs)(fn)


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
    trusted: set[str] = Field(
        {"127.0.0.1"},
        title="Trusted IPs",
        description="IPs to trust for proxy headers.",
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

    _validate_stringsets = _split_string_validator("trusted")


class HostsMiddlewareConfig(BaseModel):
    """Configuration for allowed hosts."""

    allowed: set[str] = Field(
        {"*"},
        title="Allowed hosts",
        description="Hosts allowed to make requests.",
    )

    _validate_stringsets = _split_string_validator("allowed")


class GZipCompressionConfig(BaseModel):
    """Configuration for gzip compression."""

    level: int = Field(
        9,
        ge=0,
        le=9,
        title="Level",
        description="Level of compression.",
    )


class CompressionMiddlewareConfig(BaseModel):
    """Configuration for compression."""

    threshold: int = Field(
        512,
        gt=0,
        title="Minimum size",
        description="Minimum size in bytes of response to compress.",
    )
    gzip: GZipCompressionConfig = Field(
        GZipCompressionConfig(),
        title="GZip",
        description="Configuration for gzip compression.",
    )


class CORSMiddlewareConfig(BaseModel):
    """Configuration for CORS."""

    origins: set[str] = Field(
        {"*"},
        title="Allowed origins",
        description="Origins allowed to make requests.",
    )
    methods: set[str] = Field(
        {"*"},
        title="Allowed methods",
        description="Methods allowed to be used in requests.",
    )
    headers: set[str] = Field(
        {"*"},
        title="Allowed headers",
        description="Headers allowed to be used in requests.",
    )
    credentials: bool = Field(
        False,
        title="Allow credentials",
        description="Whether to allow credentials.",
    )
    expose: set[str] = Field(
        set(),
        title="Exposed headers",
        description="Headers exposed to the client.",
    )
    age: int = Field(
        600,
        ge=0,
        title="Max age",
        description="Max age of preflight requests.",
    )

    _validate_stringsets = _split_string_validator(
        "origins", "methods", "headers", "expose"
    )


class RateLimitMiddlewareConfig(BaseModel):
    """Configuration for rate limiting."""

    unit: Literal["second", "minute", "hour", "day"] = Field(
        "minute",
        title="Unit",
        description="Unit of time to use for rate limiting.",
    )
    limit: int = Field(
        600,
        ge=0,
        title="Limit",
        description="Number of requests allowed per unit of time.",
    )


class MiddlewareConfig(BaseModel):
    """Configuration for middleware."""

    hosts: HostsMiddlewareConfig = Field(
        HostsMiddlewareConfig(),
        title="Hosts",
        description="Configuration for allowed hosts middleware.",
    )
    compression: CompressionMiddlewareConfig = Field(
        CompressionMiddlewareConfig(),
        title="Compression",
        description="Configuration for compression middleware.",
    )
    cors: CORSMiddlewareConfig = Field(
        CORSMiddlewareConfig(),
        title="CORS",
        description="Configuration for CORS middleware.",
    )
    ratelimit: RateLimitMiddlewareConfig = Field(
        RateLimitMiddlewareConfig(),
        title="Rate limit",
        description="Configuration for rate limiting middleware.",
    )


class Config(BaseConfig):
    """Configuration for the application."""

    server: ServerConfig = Field(
        ServerConfig(),
        title="Server",
        description="Configuration for the server.",
    )
    middleware: MiddlewareConfig = Field(
        MiddlewareConfig(),
        title="Middleware",
        description="Configuration for middleware.",
    )
