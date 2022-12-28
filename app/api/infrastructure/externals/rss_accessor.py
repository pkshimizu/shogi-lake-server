from datetime import datetime

from app.api.domain.models import NewsEntry
from app.api.domain.repositories import RssRepository
import feedparser


class RssAccessor(RssRepository):
    def load_news(self, url: str, provider_uid: str) -> list[NewsEntry]:
        feed = feedparser.parse(url)
        return [
            NewsEntry(
                url=entry.link,
                title=entry.title,
                published_at=self.__to_datetime_from_str(entry.updated),
                provider_uid=provider_uid,
            )
            for entry in feed.entries
        ]

    @staticmethod
    def __to_datetime_from_str(value: str) -> datetime:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
