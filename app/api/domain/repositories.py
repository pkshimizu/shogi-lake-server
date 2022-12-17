from abc import ABCMeta, abstractmethod

from app.api.domain.models import PlayerRecord, PlayerGradeRecord, TournamentTermRecord


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
