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
                published_at=entry.updated,
                provider_uid=provider_uid,
            )
            for entry in feed.entries
        ]
