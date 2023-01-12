from flask import Flask
from flask_apscheduler import APScheduler

from app.api.application import NewsCollectService, NewsFetchService

scheduler = APScheduler()


def setup_scheduler(app: Flask):
    scheduler.init_app(app)

    @scheduler.task("cron", id="job_collect_news", minute="05")
    def job_collect_news():
        from app.api.injector import injector

        news_collect_service = injector.get(NewsCollectService)
        news_collect_service.collect_shogi_federation()
        news_collect_service.collect_yomiuri_news()
        news_collect_service.collect_asahi_news()
        news_collect_service.collect_mainichi_news()
        news_collect_service.collect_hokkaido_news()

        news_fetch_service = injector.get(NewsFetchService)
        news_fetch_service.fetch_image()

    scheduler.start()
