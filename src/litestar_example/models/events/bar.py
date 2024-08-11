from typing import Literal

from litestar_example.models.base import SerializableModel
from litestar_example.models.events import types as t


class BarEventData(SerializableModel):
    """Data of a bar event."""

    bar: str
    """Bar field."""


class BarEvent(SerializableModel):
    """Bar event."""

    type: t.TypeFieldType[Literal["bar"]] = "bar"
    created_at: t.CreatedAtFieldType
    data: t.DataFieldType[BarEventData]
