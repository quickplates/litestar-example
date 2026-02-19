from typing import Literal

from pydantic import Field

from litestar_example.models.base import SerializableModel
from litestar_example.models.events.enums import EventType
from litestar_example.models.events.fields import CreatedAtField, DataField, TypeField
from litestar_example.utils.time import naiveutcnow


class TestEventData(SerializableModel):
    """Data of a test event."""

    message: str
    """Message of the test event."""


class TestEvent(SerializableModel):
    """Event that is emitted for testing purposes."""

    type: TypeField[Literal[EventType.TEST]] = EventType.TEST
    created_at: CreatedAtField = Field(default_factory=naiveutcnow)
    data: DataField[TestEventData]
