from litestar.datastructures import State as LitestarState

from litestar_example.config.models import Config


class State(LitestarState):
    """Use this class as a type hint for the state of the service."""

    config: Config
    """Configuration for the service."""
