from injector import Module, Binder

from app.api.domain.repositories import (
    MasterDataSheetRepository,
    RssRepository,
    ScrapingRepository,
)
from app.api.infrastructure.externals.master_data_sheet_accessor import (
    MasterDataSheetAccessor,
)
from app.api.infrastructure.externals.rss_accessor import RssAccessor
from app.api.infrastructure.externals.scraping_accessor import ScrapingAccessor


class ExternalModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(MasterDataSheetRepository, to=MasterDataSheetAccessor)
        binder.bind(RssRepository, to=RssAccessor)
        binder.bind(ScrapingRepository, to=ScrapingAccessor)
