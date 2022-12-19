from injector import inject

from app.api.domain.repositories import RssRepository, ScrapingRepository


class NewsCollectService:
    @inject
    def __init(
        self, rss_repository: RssRepository, scraping_repository: ScrapingRepository
    ):
        self.rss_repository = rss_repository
        self.scraping_repository = scraping_repository

    def collect_yomiuri_news(self):
        news_list = self.rss_repository.load_news(
            "https://assets.wor.jp/rss/rdf/yomiuri/latestnews.rdf"
        )

    def collect_asahi_news(self):
        news_list = self.rss_repository.load_news(
            "https://www.asahi.com/rss/asahi/shogi.rdf"
        )

    def collect_mainichi_news(self):
        news_list = self.scraping_repository.scribe_from_site(
            "https://mainichi.jp/shogi/"
        )
