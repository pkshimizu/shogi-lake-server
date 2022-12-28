from app.api.domain.models import NewsProvider
from app.api.domain.repositories import NewsProviderRepository
from app.api.infrastructure.datasources.entities import NewsProviderEntity


class NewsProviderAccessor(NewsProviderRepository):
    def get_by_uid(self, uid: str) -> NewsProvider:
        entity = NewsProviderEntity.query.filter_by(uid=uid).one()
        return self.__news_provider(entity)

    @staticmethod
    def __news_provider(entity: NewsProviderEntity) -> NewsProvider:
        return NewsProvider(uid=entity.uid, name=entity.name, rss_url=entity.rss_url)
