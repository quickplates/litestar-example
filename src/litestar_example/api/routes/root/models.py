from typing import Literal

from pydantic import Field

from litestar_example.models import SerializableModel


class GetResponse(SerializableModel):
    """Example GET response."""

    foo: Literal["bar"] = Field(
        ...,
        title="Foo",
        description="Should be 'bar'.",
    )
