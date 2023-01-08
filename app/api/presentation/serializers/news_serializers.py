from dataclasses import dataclass

from app.api.domain.models import Pagination, News
from app.api.presentation.serializers.base import (
    Resource,
    PaginationResponse,
    Request,
)


@dataclass
class NewsProviderResource(Resource):
    uid: str
    name: str


@dataclass
class NewsTagResource(Resource):
    uid: str
    name: str


@dataclass
class NewsResource(Resource):
    uid: str
    url: str
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
        super().__init__(pagination, 200)
