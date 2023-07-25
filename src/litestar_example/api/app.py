from litestar import Litestar, Router
from litestar.openapi import OpenAPIConfig

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
            openapi_config=self._build_openapi_config(),
            state=self._build_initial_state(),
        )
