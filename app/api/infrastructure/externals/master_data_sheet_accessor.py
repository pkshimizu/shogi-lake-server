from app.api.domain.models import Player
from app.api.domain.repositories import MasterDataSheetRepository


class MasterDataSheetAccessor(MasterDataSheetRepository):
    def load_players(self) -> list[Player]:
        pass
