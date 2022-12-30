from injector import inject

from app.api.application.decorators import transaction
from app.api.domain.models import NewsEntry, NewsTag, NewsProvider
from app.api.domain.repositories import (
    RssRepository,
    ScrapingRepository,
    NewsTagRepository,
    NewsProviderRepository,
    NewsRepository,
)


class NewsCollectService:
    @inject
    def __init__(
        self,
        rss_repository: RssRepository,
        scraping_repository: ScrapingRepository,
        news_repository: NewsRepository,
        news_tag_repository: NewsTagRepository,
        news_provider_repository: NewsProviderRepository,
    ):
        self.rss_repository = rss_repository
        self.scraping_repository = scraping_repository
        self.news_repository = news_repository
        self.news_tag_repository = news_tag_repository
        self.news_provider_repository = news_provider_repository

    @transaction
    def collect_shogi_federation(self):
        provider = self.news_provider_repository.get_by_uid(
            NewsProvider.SHOGI_FEDERATION_UID
        )
        news_list = self.rss_repository.load_news(
            url=provider.rss_url,
            provider_uid=provider.uid,
        )
        registered_news_tags = self.news_tag_repository.get_all()
        for news in news_list:
            news_tags = self.__make_tags(news, registered_news_tags)
            if len(news_tags) > 0:
                self.news_repository.save_news(news, news_tags)

    @transaction
    def collect_yomiuri_news(self):
        provider = self.news_provider_repository.get_by_uid(
            NewsProvider.YOMIURI_NEWS_UID
        )
        news_list = self.rss_repository.load_news(
            url=provider.rss_url,
            provider_uid=provider.uid,
        )
        registered_news_tags = self.news_tag_repository.get_all()
        for news in news_list:
            news_tags = self.__make_tags(news, registered_news_tags)
            if len(news_tags) > 0:
                self.news_repository.save_news(news, news_tags)

    @transaction
    def collect_asahi_news(self):
        provider = self.news_provider_repository.get_by_uid(NewsProvider.ASAHI_NEWS_UID)
        news_list = self.rss_repository.load_news(
            url=provider.rss_url, provider_uid=provider.uid
        )
        registered_news_tags = self.news_tag_repository.get_all()
        for news in news_list:
            news_tags = self.__make_tags(news, registered_news_tags)
            if len(news_tags) > 0:
                self.news_repository.save_news(news, news_tags)

    @transaction
    def collect_mainichi_news(self):
        news_list = self.scraping_repository.scribe_from_site(
            "https://mainichi.jp/shogi/",
            "//*[@id='article-list']/ul/li/a",
            "//*[@id='article-list']/ul/li/a"
            "/div[@class='articlelist-item']/div[@class='articlelist-detail']/h3",
            "//*[@id='article-list']/ul/li/a"
            "/div[@class='articlelist-item']/div[@class='articlelist-detail']"
            "/div[@class='articletag mb-8']/span[contains(@class,'articletag-date')]",
            "%Y/%m/%d %H:%M",
            NewsProvider.MAINICHI_NEWS_UID,
        )
        registered_news_tags = self.news_tag_repository.get_all()
        for news in news_list:
            news_tags = self.__make_tags(news, registered_news_tags)
            if len(news_tags) > 0:
                self.news_repository.save_news(news, news_tags)

    @staticmethod
    def __make_tags(news_entry: NewsEntry, news_tags: list[NewsTag]) -> list[NewsTag]:
        return list(filter(lambda tag: tag.name in news_entry.title, news_tags))
