from conversion import run_ffmpeg
import click


@click.command()
@click.argument("input", type=str)
@click.option(
    "--activation-bytes",
    type=str,
    help="Activation bytes needed to convert .aax files.",
)
def convert(input: str, activation_bytes: str):
    result = run_ffmpeg(filepath=input, activation_bytes=activation_bytes)
    if result:
        click.echo(result)


if __name__ == "__main__":
    convert()
