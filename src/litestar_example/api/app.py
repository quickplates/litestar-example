from litestar import Litestar, Router
from litestar.config.allowed_hosts import AllowedHostsConfig
from litestar.config.compression import CompressionConfig
from litestar.config.cors import CORSConfig
from litestar.middleware.rate_limit import RateLimitConfig
from litestar.openapi import OpenAPIConfig
from litestar.types import Middleware

from litestar_example.api.routes.router import router
from litestar_example.builder import Builder
from litestar_example.config import Config
from litestar_example.state import State


class AppBuilder(Builder[Litestar]):
    """Builds the app.

    Args:
        config: Config object.
    """

    def __init__(self, config: Config) -> None:
        self._config = config

    def _get_route_handlers(self) -> list[Router]:
        return [router]

    def _build_hosts_config(self) -> AllowedHostsConfig:
        hosts = self._config.middleware.hosts
        return AllowedHostsConfig(
            allowed_hosts=list(hosts.allowed),
        )

    def _build_compression_config(self) -> CompressionConfig:
        compression = self._config.middleware.compression
        return CompressionConfig(
            backend="gzip",
            minimum_size=compression.threshold,
            gzip_compress_level=compression.gzip.level,
        )

    def _build_cors_config(self) -> CORSConfig:
        cors = self._config.middleware.cors
        return CORSConfig(
            allow_origins=list(cors.origins),
            allow_methods=list(cors.methods),
            allow_headers=list(cors.headers),
            allow_credentials=cors.credentials,
            expose_headers=list(cors.expose),
            max_age=cors.age,
        )

    def _build_rate_limit_middleware_config(self) -> RateLimitConfig:
        ratelimit = self._config.middleware.ratelimit
        return RateLimitConfig(
            rate_limit=(
                ratelimit.unit,
                ratelimit.limit,
            ),
        )

    def _build_middlewares(self) -> list[Middleware]:
        return [
            self._build_rate_limit_middleware_config().middleware,
        ]

    def _build_openapi_config(self) -> OpenAPIConfig:
        return OpenAPIConfig(
            title="litestar-example",
            version="0.1.0",
            description="Litestar project example 🌠",
        )

    def _build_initial_state(self) -> State:
        return State({"config": self._config})

    def build(self) -> Litestar:
        return Litestar(
            route_handlers=self._get_route_handlers(),
            allowed_hosts=self._build_hosts_config(),
            compression_config=self._build_compression_config(),
            cors_config=self._build_cors_config(),
            middleware=self._build_middlewares(),
            openapi_config=self._build_openapi_config(),
            state=self._build_initial_state(),
        )
