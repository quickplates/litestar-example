from datetime import datetime
from typing import Annotated, Literal, TypeVar

from pydantic import Field, RootModel

from litestar_example.models.base import SerializableModel
from litestar_example.models.data import Foo
from litestar_example.time import naiveutcnow

TypeType = TypeVar("TypeType")
DataType = TypeVar("DataType", bound=SerializableModel)

TypeFieldType = Annotated[
    TypeType,
    Field(description="Type of the event."),
]
CreatedAtFieldType = Annotated[
    datetime,
    Field(
        default_factory=naiveutcnow, description="Time at which the event was created."
    ),
]
DataFieldType = Annotated[
    DataType,
    Field(description="Data of the event."),
]


class DummyEventData(SerializableModel):
    """Data of a dummy event."""

    pass


class DummyEvent(SerializableModel):
    """Dummy event that exists only so that there can be two types in discriminated union."""

    type: TypeFieldType[Literal["dummy"]] = Field(
        "dummy",
        title="DummyEvent.Type",
    )
    created_at: CreatedAtFieldType = Field(
        ...,
        title="DummyEvent.CreatedAt",
    )
    data: DataFieldType[DummyEventData] = Field(
        DummyEventData(),
        title="DummyEvent.Data",
    )


class FooEventData(SerializableModel):
    """Data of a foo event."""

    foo: Foo = Field(
        ...,
        title="FooEventData.Foo",
        description="Example Foo object.",
    )


class FooEvent(SerializableModel):
    """Foo event."""

    type: TypeFieldType[Literal["foo"]] = Field(
        "foo",
        title="FooEvent.Type",
    )
    created_at: CreatedAtFieldType = Field(
        ...,
        title="FooEvent.CreatedAt",
    )
    data: DataFieldType[FooEventData] = Field(
        ...,
        title="FooEvent.Data",
    )


Event = Annotated[DummyEvent | FooEvent, Field(..., discriminator="type")]
ParsableEvent = RootModel[Event]
