from typing import Annotated

from pydantic import Field, RootModel

from litestar_example.models.events.bar import BarEvent
from litestar_example.models.events.foo import FooEvent

Event = Annotated[FooEvent | BarEvent, Field(..., discriminator="type")]
ParsableEvent = RootModel[Event]
