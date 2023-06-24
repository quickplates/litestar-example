from rich.console import Console

from litestar_example.builder import Builder
from litestar_example.config import Config


class ConsoleBuilder(Builder[Console]):
    """Builds the console.

    Args:
        config: Config object.
    """

    def __init__(self, config: Config) -> None:
        self._config = config

    def build(self) -> Console:
        return Console()


class EmergencyConsoleBuilder(Builder[Console]):
    """Builds the emergency console."""

    def build(self) -> Console:
        return Console()
