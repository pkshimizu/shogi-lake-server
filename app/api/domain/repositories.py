from abc import ABCMeta, abstractmethod
from types import FunctionType

from app.api.domain.models import (
    PlayerRecord,
    PlayerGradeRecord,
    TournamentTermRecord,
    NewsEntry,
    NewsTag,
    NewsProvider,
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
    def load_news(self, url: str, provider_uid: str) -> list[NewsEntry]:
        pass


class ScrapingRepository(metaclass=ABCMeta):
    @abstractmethod
    def scribe_from_site(
        self,
        url: str,
        url_xpath: str,
        title_xpath: str,
        date_xpath: str,
        date_converter: FunctionType,
        provider_uid: str,
    ) -> list[NewsEntry]:
        pass


class NewsRepository(metaclass=ABCMeta):
    @abstractmethod
    def save_news(self, news: NewsEntry, news_tags: list[NewsTag]):
        pass


class NewsTagRepository(metaclass=ABCMeta):
    @abstractmethod
    def save_tags(self, names: list[str]):
        pass

    def get_all(self) -> list[NewsTag]:
        pass


class NewsProviderRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_by_uid(self, uid: str) -> NewsProvider:
        pass
