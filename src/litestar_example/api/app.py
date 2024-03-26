from importlib import metadata

from litestar import Litestar, Router
from litestar.channels import ChannelsPlugin
from litestar.channels.backends.memory import MemoryChannelsBackend
from litestar.contrib.pydantic import PydanticPlugin
from litestar.openapi import OpenAPIConfig
from litestar.plugins import PluginProtocol

from litestar_example.api.routes.router import router
from litestar_example.config.models import Config
from litestar_example.state import State


class AppBuilder:
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
            title="litestar-example app",
            version=metadata.version("litestar_example"),
            description="Litestar app example 🌠",
        )

    def _build_channels_plugin(self) -> ChannelsPlugin:
        return ChannelsPlugin(
            backend=MemoryChannelsBackend(),
            channels=["events"],
        )

    def _build_pydantic_plugin(self) -> PydanticPlugin:
        return PydanticPlugin(
            prefer_alias=True,
        )

    def _build_plugins(self) -> list[PluginProtocol]:
        return [
            self._build_channels_plugin(),
            self._build_pydantic_plugin(),
        ]

    def _build_initial_state(self) -> State:
        return State(
            {
                "config": self._config,
            }
        )

    def build(self) -> Litestar:
        return Litestar(
            route_handlers=self._get_route_handlers(),
            openapi_config=self._build_openapi_config(),
            plugins=self._build_plugins(),
            state=self._build_initial_state(),
        )
