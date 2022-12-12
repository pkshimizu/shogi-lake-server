from injector import Module, Binder

from app.api.domain.repositories import PlayerRepository, PlayerGradeRepository
from app.api.infrastructure.datasources.player_accessor import PlayerAccessor
from app.api.infrastructure.datasources.player_grade_accessor import PlayerGradeAccessor


class DatasourceModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(PlayerGradeRepository, to=PlayerGradeAccessor)
        binder.bind(PlayerRepository, to=PlayerAccessor)
        pass
