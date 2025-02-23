from collections.abc import AsyncIterator

from litestar_example.models.base import datamodel
from litestar_example.models.events.event import Event


@datamodel
class SubscribeRequest:
    """Request to subscribe."""

    pass


@datamodel
class SubscribeResponse:
    """Response for subscribe."""

    events: AsyncIterator[Event]
    """Stream of events."""
