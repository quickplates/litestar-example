from datetime import datetime
from typing import Annotated, TypeVar

from pydantic import Field

from litestar_example.models.base import SerializableModel
from litestar_example.utils.time import naiveutcnow

TypeType = TypeVar("TypeType")

DataType = TypeVar("DataType", bound=SerializableModel)

TypeFieldType = Annotated[
    TypeType,
    Field(
        description="Type of the event.",
    ),
]

CreatedAtFieldType = Annotated[
    datetime,
    Field(
        default_factory=naiveutcnow,
        description="Time at which the event was created.",
    ),
]

DataFieldType = Annotated[
    DataType,
    Field(
        description="Data of the event.",
    ),
]
