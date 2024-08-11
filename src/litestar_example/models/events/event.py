from typing import Annotated

from pydantic import Field, RootModel

from litestar_example.models.events import bar as be
from litestar_example.models.events import foo as fe

Event = Annotated[be.BarEvent | fe.FooEvent, Field(..., discriminator="type")]
ParsableEvent = RootModel[Event]
