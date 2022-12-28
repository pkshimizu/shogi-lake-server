from injector import Module, Binder

from app.api.domain.repositories import (
    PlayerRepository,
    PlayerGradeRepository,
    TournamentRepository,
    NewsTagRepository,
    NewsProviderRepository,
    NewsRepository,
)
from app.api.infrastructure.datasources.news_accessor import NewsAccessor
from app.api.infrastructure.datasources.news_provider_accessor import (
    NewsProviderAccessor,
)
from app.api.infrastructure.datasources.news_tag_accessor import NewsTagAccessor
from app.api.infrastructure.datasources.player_accessor import PlayerAccessor
from app.api.infrastructure.datasources.player_grade_accessor import PlayerGradeAccessor
from app.api.infrastructure.datasources.tournament_accessor import TournamentAccessor


class DatasourceModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(PlayerGradeRepository, to=PlayerGradeAccessor)
        binder.bind(PlayerRepository, to=PlayerAccessor)
        binder.bind(TournamentRepository, to=TournamentAccessor)
        binder.bind(NewsRepository, to=NewsAccessor)
        binder.bind(NewsTagRepository, to=NewsTagAccessor)
        binder.bind(NewsProviderRepository, to=NewsProviderAccessor)
