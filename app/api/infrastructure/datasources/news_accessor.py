from sqlalchemy import desc

from app.api.database import db
from app.api.domain.models import NewsTag, NewsEntry, News, Pagination
from app.api.domain.repositories import NewsRepository
from app.api.infrastructure.datasources.entities import (
    NewsTagEntity,
    NewsEntity,
    NewsProviderEntity,
)


class NewsAccessor(NewsRepository):
    def save_news(self, news: NewsEntry, news_tags: list[NewsTag]):
        news_entity = NewsEntity.query.filter_by(url=news.url).one_or_none()
        news_tag_uid_list = [tag.uid for tag in news_tags]
        news_provider = NewsProviderEntity.query.filter_by(uid=news.provider_uid).one()
        news_tag_entities = NewsTagEntity.query.filter(
            NewsTagEntity.uid.in_(news_tag_uid_list)
        ).all()
        if news_entity is None:
            news_entity = NewsEntity()
            news_entity.url = news.url
        news_entity.title = news.title
        news_entity.news_provider = news_provider
        news_entity.news_tags = news_tag_entities
        news_entity.published_at = news.published_at
        if news_entity.id is None:
            db.session.add(news_entity)

    def get_all_no_image(self) -> list[News]:
        entities = NewsEntity.query.filter_by(image_url=None).all()
        return self.to_news_list(entities)

    def save_image(self, news_id: int, image_url: str):
        entity = NewsEntity.query.filter_by(id=news_id).one()
        entity.image_url = image_url

    def paginate(self, page: int, per_page: int) -> Pagination[News]:
        paginate = NewsEntity.query.order_by(desc(NewsEntity.published_at)).paginate(
            page=page, per_page=per_page
        )
        return Pagination.to_model(self.to_news_list(paginate.items), paginate)

    @staticmethod
    def to_news_list(entities: list[NewsEntity]) -> list[News]:
        return [entity.to_model() for entity in entities]
