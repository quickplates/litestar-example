from typing import Literal

from pydantic import Field

from litestar_example.models.base import SerializableModel


class Foo(SerializableModel):
    """Foo model."""

    foo: Literal["bar"] = Field(
        "bar",
        title="Foo.Foo",
        description="Value of foo.",
    )
