from dataclasses import dataclass

from app.api.domain.models import Pagination, News, NewsTag, NewsProvider
from app.api.presentation.serializers.base import (
    Resource,
    PaginationResponse,
    Request,
)


@dataclass
class NewsProviderResource(Resource):
    def __init__(self, news_provider: NewsProvider):
        self.uid = news_provider.uid
        self.name = news_provider.name

    uid: str
    name: str


@dataclass
class NewsTagResource(Resource):
    def __init__(self, news_tag: NewsTag):
        self.uid = news_tag.uid
        self.name = news_tag.name

    uid: str
    name: str


@dataclass
class NewsResource(Resource):
    def __init__(self, news: News):
        self.uid = news.uid
        self.url = news.uid
        self.image_url = news.image_url
        self.title = news.title
        self.published_at = self.datetime_str(news.published_at)
        self.provider = NewsProviderResource(news.provider)
        self.tags = [NewsTagResource(tag) for tag in news.tags]

    uid: str
    url: str
    image_url: str
    title: str
    published_at: str
    provider: NewsProviderResource
    tags: list[NewsTagResource]


class NewsListRequest(Request):
    def __init__(self):
        super().__init__()
        self.page = self.get_query_int("page", 1)

    page: int


@dataclass
class NewsListResponse(PaginationResponse):
    def __init__(self, pagination: Pagination[News]):
        items = [NewsResource(item) for item in pagination.items]
        super().__init__(items, pagination, 200)
