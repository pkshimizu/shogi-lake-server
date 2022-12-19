from abc import ABCMeta, abstractmethod

from app.api.domain.models import (
    PlayerRecord,
    PlayerGradeRecord,
    TournamentTermRecord,
    News,
)


class MasterDataSheetRepository(metaclass=ABCMeta):
    @abstractmethod
    def load_grades(self) -> list[PlayerGradeRecord]:
        pass

    @abstractmethod
    def load_players(self) -> list[PlayerRecord]:
        pass

    @abstractmethod
    def load_tournaments(self) -> list[TournamentTermRecord]:
        pass


class PlayerGradeRepository(metaclass=ABCMeta):
    @abstractmethod
    def save_from_records(self, grade_records: list[PlayerGradeRecord]):
        pass


class PlayerRepository(metaclass=ABCMeta):
    @abstractmethod
    def save_from_records(self, player_records: list[PlayerRecord]):
        pass


class TournamentRepository(metaclass=ABCMeta):
    @abstractmethod
    def save_from_records(self, tournament_term_records: list[TournamentTermRecord]):
        pass


class RssRepository(metaclass=ABCMeta):
    @abstractmethod
    def load_news(self, url: str) -> list[News]:
        pass


class ScrapingRepository(metaclass=ABCMeta):
    @abstractmethod
    def scribe_from_site(self, url: str) -> list[News]:
        pass
