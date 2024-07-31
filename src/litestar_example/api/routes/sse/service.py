from collections.abc import AsyncGenerator

from litestar.channels import ChannelsPlugin

from litestar_example.api.routes.sse import models as m
from litestar_example.models.events import ParsableEvent


class Service:
    """Service for the sse endpoint."""

    def __init__(self, channels: ChannelsPlugin) -> None:
        self._channels = channels

    async def _subscribe(self) -> AsyncGenerator[str]:
        async with self._channels.start_subscription("events") as subscriber:
            async for event in subscriber.iter_events():
                event = ParsableEvent.model_validate_json(event)
                yield event.root.model_dump_json(by_alias=True)

    async def subscribe(self, request: m.SubscribeRequest) -> m.SubscribeResponse:
        """Subscribe to app events."""

        return m.SubscribeResponse(messages=self._subscribe())
