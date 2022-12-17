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


@click.command("tournament", help="Import Tournaments")
def import_tournament():
    from app.api.injector import injector

    import_service = injector.get(ImportService)
    import_service.import_tournament()


def setup_commands(app: Flask):
    import_commands = AppGroup("import")
    import_commands.add_command(import_grade)
    import_commands.add_command(import_player)
    import_commands.add_command(import_tournament)

    app.cli.add_command(import_commands)
