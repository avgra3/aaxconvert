from .conversion import run_ffmpeg
import click
import os
import sys

ACTIVATION_BYTES = os.getenv("ACTIVATION_BYTES")


@click.group()
def main():
    pass


@main.command()
@click.argument("input", type=str)
@click.option(
    "--activation-bytes",
    type=str,
    help="Activation bytes needed to convert .aax files.",
    default=ACTIVATION_BYTES,
)
def convert(input: str, activation_bytes: str):
    if not activation_bytes:
        sys.exit(
            f"""ERROR: Activation bytes is not located as an environment variable and not provided as an input.

            Please do one of two things:

            1. Add an environment variable to your system as ACTIVATION_BYTES. This is the preferred method as it won't be needed as a manual input if an environment variable.
            2. Include your activation bytes value when running this command."""
        )
    result = run_ffmpeg(filepath=input, activation_bytes=activation_bytes)
    if result:
        click.echo(result)


if __name__ == "__main__":
    main()
