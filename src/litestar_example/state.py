from litestar.datastructures import State as LitestarState

from litestar_example.config import Config


class State(LitestarState):
    """Use this class as a type hint for the state of your application.

    Attributes:
        config: The configuration for the application.
    """

    config: Config
