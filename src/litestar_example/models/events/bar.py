from typing import Literal

from pydantic import Field

from litestar_example.models.base import SerializableModel
from litestar_example.models.events import types as t
from litestar_example.utils.time import naiveutcnow


class BarEventData(SerializableModel):
    """Data of a bar event."""

    bar: str
    """Bar field."""


class BarEvent(SerializableModel):
    """Bar event."""

    type: t.TypeField[Literal["bar"]] = "bar"
    created_at: t.CreatedAtField = Field(default_factory=naiveutcnow)
    data: t.DataField[BarEventData]
