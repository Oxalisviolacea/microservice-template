import click
from . import __version__

@click.command()
@click.version_option(version=__version__)
def main():
    """Return 'Hello, World!'"""
    click.echo("Hello, world!")