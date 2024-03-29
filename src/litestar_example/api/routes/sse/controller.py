from litestar import Controller as BaseController
from litestar import get
from litestar.channels import ChannelsPlugin
from litestar.di import Provide
from litestar.response import ServerSentEvent

from litestar_example.api.routes.sse.service import Service


class DependenciesBuilder:
    """Builder for the dependencies of the controller."""

    async def _build_service(self, channels: ChannelsPlugin) -> Service:
        return Service(channels)

    def build(self) -> dict[str, Provide]:
        return {
            "service": Provide(self._build_service),
        }


class Controller(BaseController):
    """Controller for the sse endpoint."""

    dependencies = DependenciesBuilder().build()

    @get(
        summary="Get SSE stream",
        description="Get a stream of Server-Sent Events.",
    )
    async def subscribe(self, service: Service) -> ServerSentEvent:
        return ServerSentEvent(service.subscribe())
