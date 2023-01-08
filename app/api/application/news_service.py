from injector import inject

from app.api.domain.models import Pagination, News
from app.api.domain.repositories import NewsRepository


class NewsService:
    @inject
    def __init__(self, news_repository: NewsRepository):
        self.news_repository = news_repository

    def paginate(self, page: int, per_page: int) -> Pagination[News]:
        return self.news_repository.paginate(page, per_page)
