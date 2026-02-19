from typing import Annotated

from pydantic import Field

from litestar_example.models.events import test

type Event = Annotated[
    test.TestEvent,
    Field(discriminator="type"),
]
