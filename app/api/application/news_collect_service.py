from injector import inject

from app.api.domain.models import NewsEntry, NewsTag
from app.api.domain.repositories import (
    RssRepository,
    ScrapingRepository,
    NewsTagRepository,
)


class NewsCollectService:
    @inject
    def __init__(
        self,
        rss_repository: RssRepository,
        scraping_repository: ScrapingRepository,
        news_tag_repository: NewsTagRepository,
    ):
        self.rss_repository = rss_repository
        self.scraping_repository = scraping_repository
        self.news_tag_repository = news_tag_repository

    def collect_yomiuri_news(self):
        news_list = self.rss_repository.load_news(
            url="https://assets.wor.jp/rss/rdf/yomiuri/latestnews.rdf",
            provider_uid="yomiuri",
        )
        registered_news_tags = self.news_tag_repository.get_all()
        for news in news_list:
            news_tags = self.__make_tags(news, registered_news_tags)

    def collect_asahi_news(self):
        news_list = self.rss_repository.load_news(
            url="https://www.asahi.com/rss/asahi/shogi.rdf", provider_uid="asahi"
        )
        registered_news_tags = self.news_tag_repository.get_all()
        for news in news_list:
            news_tags = self.__make_tags(news, registered_news_tags)

    def collect_mainichi_news(self):
        news_list = self.scraping_repository.scribe_from_site(
            "https://mainichi.jp/shogi/"
        )
        registered_news_tags = self.news_tag_repository.get_all()
        for news in news_list:
            news_tags = self.__make_tags(news, registered_news_tags)

    @staticmethod
    def __make_tags(news_entry: NewsEntry, news_tags: list[NewsTag]) -> list[NewsTag]:
        return list(filter(lambda tag: tag.name in news_entry.title, news_tags))
