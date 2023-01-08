from flask import Blueprint
from injector import inject

from app.api.application.news_service import NewsService
from app.api.presentation.serializers.news_serializers import (
    NewsListResponse,
    NewsListRequest,
)

news_module = Blueprint("news", __name__, url_prefix="/news")


@news_module.route("")
@inject
def get_list(news_service: NewsService):
    request = NewsListRequest()
    pagination = news_service.paginate(request.page, 30)
    return NewsListResponse(pagination).data()
