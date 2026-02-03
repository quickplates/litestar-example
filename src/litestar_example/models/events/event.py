from typing import Annotated

from pydantic import Field

from litestar_example.models.events import bar as be
from litestar_example.models.events import foo as fe

type Event = Annotated[be.BarEvent | fe.FooEvent, Field(discriminator="type")]
