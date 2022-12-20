from app.api.domain.models import News
from app.api.domain.repositories import ScrapingRepository


class ScrapingAccessor(ScrapingRepository):
    def scribe_from_site(self, url: str) -> list[News]:
        pass
