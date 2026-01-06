from collections.abc import AsyncGenerator, Generator
from contextlib import contextmanager

from litestar_example.api.routes.sse import errors as e
from litestar_example.api.routes.sse import models as m
from litestar_example.services.events import errors as ee
from litestar_example.services.events import models as em
from litestar_example.services.events.service import EventsService


class Service:
    """Service for the sse endpoint."""

    def __init__(self, events: EventsService) -> None:
        self._events = events

    @contextmanager
    def _handle_errors(self) -> Generator[None]:
        try:
            yield
        except ee.ServiceError as ex:
            raise e.ServiceError(str(ex)) from ex

    async def _subscribe(self) -> AsyncGenerator[str]:
        req = em.SubscribeRequest()

        with self._handle_errors():
            res = await self._events.subscribe(req)

            async for event in res.events:
                yield event.model_dump_json(by_alias=True)

    async def subscribe(self, request: m.SubscribeRequest) -> m.SubscribeResponse:
        """Subscribe to event messages."""
        messages = self._subscribe()

        return m.SubscribeResponse(
            messages=messages,
        )
