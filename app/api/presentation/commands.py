import click
from flask import Flask
from flask.cli import AppGroup

from app.api.application import ImportService


@click.command("grade", help="Import Shogi Grades")
def import_grade():
    from app.api.injector import injector

    import_service = injector.get(ImportService)
    import_service.import_player_grade()


@click.command("player", help="Import Shogi Player")
def import_player():
    from app.api.injector import injector

    import_service = injector.get(ImportService)
    import_service.import_player()


def setup_commands(app: Flask):
    import_commands = AppGroup("import")
    import_commands.add_command(import_grade)
    import_commands.add_command(import_player)

    app.cli.add_command(import_commands)
