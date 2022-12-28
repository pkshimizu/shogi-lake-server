from app.api.database import db
from app.api.domain.models import NewsTag
from app.api.domain.repositories import NewsTagRepository
from app.api.infrastructure.datasources.entities import NewsTagEntity


class NewsTagAccessor(NewsTagRepository):
    def save_tags(self, names: list[str]):
        tags = NewsTagEntity.query.all()
        tag_names = [tag.name for tag in tags]
        new_tags = []
        for name in names:
            if name in tag_names:
                continue
            news_tag = NewsTagEntity()
            news_tag.name = name
            new_tags.append(news_tag)
        db.session.add_all(new_tags)

    def get_all(self) -> list[NewsTag]:
        tags = NewsTagEntity.query.filter(NewsTagEntity.deleted_at is not None).all()
        return [self.__to_news_tag(tag) for tag in tags]

    @staticmethod
    def __to_news_tag(entity: NewsTagEntity) -> NewsTag:
        return NewsTag(uid=entity.uid, name=entity.name)
