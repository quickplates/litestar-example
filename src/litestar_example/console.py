from rich.console import Console

from litestar_example.builder import Builder


class EmergencyConsoleBuilder(Builder[Console]):
    """Builds the emergency console."""

    def build(self) -> Console:
        return Console()
