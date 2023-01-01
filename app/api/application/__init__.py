from injector import Module, Binder

from app.api.application.import_service import ImportService
from app.api.application.news_collect_service import NewsCollectService
from app.api.application.news_fetch_service import NewsFetchService


class ApplicationServiceModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(ImportService, to=ImportService)
        binder.bind(NewsCollectService, to=NewsCollectService)
        binder.bind(NewsFetchService, to=NewsFetchService)
