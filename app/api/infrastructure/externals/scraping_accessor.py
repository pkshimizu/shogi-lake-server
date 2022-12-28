from app.api.domain.models import NewsEntry
from app.api.domain.repositories import ScrapingRepository


class ScrapingAccessor(ScrapingRepository):
    def scribe_from_site(self, url: str) -> list[NewsEntry]:
        pass
