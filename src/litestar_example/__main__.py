from typing import Optional

import typer

from litestar_example.cli import CliBuilder
from litestar_example.config import ConfigBuilder, ConfigError
from litestar_example.console import ConsoleBuilder, EmergencyConsoleBuilder
from litestar_example.foo import foo

cli = CliBuilder().build()


@cli.command()
def main(
    config_file: Optional[typer.FileText] = typer.Option(
        None,
        "--config-file",
        "-C",
        dir_okay=False,
        help="Configuration file.",
    ),
    config_overrides: Optional[list[str]] = typer.Option(
        None,
        "--config",
        "-c",
        help="Configuration entries.",
    ),
) -> None:
    """Main entry point."""

    try:
        config = ConfigBuilder(config_file, config_overrides).build()
    except ConfigError as e:
        console = EmergencyConsoleBuilder().build()
        console.print("Failed to load config!")
        console.print_exception()
        raise typer.Exit(1) from e

    console = ConsoleBuilder(config).build()

    console.print("Config loaded!")

    console.print(f"Config: {config}")
    console.print(f"foo() = {foo()}")


if __name__ == "__main__":
    cli()
