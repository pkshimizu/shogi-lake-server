from dataclasses import dataclass

from app.api.presentation.serializers.base import Response, Resource


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


@dataclass
class NewsListResponse(Response):
    def __init__(self):
        super().__init__(200)
        self.news_list = []

    news_list: list[NewsResource]
