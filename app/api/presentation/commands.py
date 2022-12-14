import click
from flask import Flask
from flask.cli import AppGroup

from app.api.application import ImportService, NewsCollectService, NewsFetchService


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


@click.command("news", help="Collect News")
def collect_news():
    from app.api.injector import injector

    news_collect_service = injector.get(NewsCollectService)
    news_collect_service.collect_shogi_federation()
    news_collect_service.collect_yomiuri_news()
    news_collect_service.collect_asahi_news()
    news_collect_service.collect_mainichi_news()
    news_collect_service.collect_hokkaido_news()


@click.command("news:image", help="Fetch News Image")
def fetch_news_image():
    from app.api.injector import injector

    news_fetch_service = injector.get(NewsFetchService)
    news_fetch_service.fetch_image()


def setup_commands(app: Flask):
    import_commands = AppGroup("import", help="Import data")
    import_commands.add_command(import_grade)
    import_commands.add_command(import_player)
    import_commands.add_command(import_tournament)

    collect_commands = AppGroup("collect", help="Collect data")
    collect_commands.add_command(collect_news)

    fetch_commands = AppGroup("fetch", help="Fetch data")
    fetch_commands.add_command(fetch_news_image)

    app.cli.add_command(import_commands)
    app.cli.add_command(collect_commands)
    app.cli.add_command(fetch_commands)
