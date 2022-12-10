from injector import Module, Binder

from app.api.domain.repositories import MasterDataSheetRepository
from app.api.infrastructure.externals.master_data_sheet_accessor import (
    MasterDataSheetAccessor,
)


class ExternalModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(MasterDataSheetRepository, to=MasterDataSheetAccessor)
