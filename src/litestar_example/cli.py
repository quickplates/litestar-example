from typer import Typer

from litestar_example.builder import Builder


class CliBuilder(Builder[Typer]):
    """Builds the CLI app."""

    def build(self) -> Typer:
        return Typer()
