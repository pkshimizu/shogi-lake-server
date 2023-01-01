from injector import inject

from app.api.application.decorators import transaction
from app.api.domain.repositories import NewsRepository, ScrapingRepository


class NewsFetchService:
    @inject
    def __init__(
        self,
        news_repository: NewsRepository,
        scraping_repository: ScrapingRepository,
    ):
        self.news_repository = news_repository
        self.scraping_repository = scraping_repository

    @transaction
    def fetch_image(self):
        news_list = self.news_repository.get_all_no_image()
        for news in news_list:
            image_url = self.scraping_repository.scribe_image_from_site(news.url)
            self.news_repository.save_image(news.id, image_url)
