from collections.abc import AsyncGenerator

from litestar.channels import ChannelsPlugin

from litestar_example.api.routes.sse.models import SubscribeMessage
from litestar_example.models.events import ParsableEvent


class Service:
    """Service for the sse endpoint."""

    def __init__(self, channels: ChannelsPlugin) -> None:
        self._channels = channels

    async def subscribe(self) -> AsyncGenerator[SubscribeMessage, None]:
        """Subscribe to app events."""

        async with self._channels.start_subscription("events") as subscriber:
            async for event in subscriber.iter_events():
                event = ParsableEvent.model_validate_json(event)
                yield event.root.model_dump_json(by_alias=True)
