import click
from flask import Flask
from flask.cli import AppGroup


@click.command("player", help="Import Shogi Player")
def import_player():
    pass


def setup_commands(app: Flask):
    import_commands = AppGroup("import")
    import_commands.add_command(import_player)

    app.cli.add_command(import_commands)
