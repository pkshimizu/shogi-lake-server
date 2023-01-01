from app.api.application.decorators import transaction
from app.api.domain.repositories import NewsRepository


class NewsFetchService:
    def __init__(self, news_repository: NewsRepository):
        self.news_repository = news_repository

    @transaction
    def fetch_image(self):
        news_list = self.news_repository.get_all_no_image()
