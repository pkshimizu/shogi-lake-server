from abc import ABCMeta, abstractmethod

from app.api.domain.models import Player


class MasterDataSheetRepository(metaclass=ABCMeta):
    @abstractmethod
    def load_players(self) -> list[Player]:
        pass
