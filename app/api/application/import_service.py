from injector import inject

from app.api.application.decorators import transaction
from app.api.domain.repositories import (
    MasterDataSheetRepository,
    PlayerRepository,
    PlayerGradeRepository,
    TournamentRepository,
    NewsTagRepository,
)


class ImportService:
    @inject
    def __init__(
        self,
        master_data_sheet_repository: MasterDataSheetRepository,
        player_grade_repository: PlayerGradeRepository,
        player_repository: PlayerRepository,
        tournament_repository: TournamentRepository,
        news_tag_repository: NewsTagRepository,
    ):
        self.master_data_sheet_repository = master_data_sheet_repository
        self.player_grade_repository = player_grade_repository
        self.player_repository = player_repository
        self.tournament_repository = tournament_repository
        self.news_tag_repository = news_tag_repository

    @transaction
    def import_player_grade(self) -> None:
        grade_records = self.master_data_sheet_repository.load_grades()
        self.player_grade_repository.save_from_records(grade_records)

    @transaction
    def import_player(self) -> None:
        player_records = self.master_data_sheet_repository.load_players()
        self.player_repository.save_from_records(player_records)
        player_names = [player.name for player in player_records]
        self.news_tag_repository.save_tags(player_names)

    @transaction
    def import_tournament(self):
        tournament_records = self.master_data_sheet_repository.load_tournaments()
        self.tournament_repository.save_from_records(tournament_records)
        tournament_names = [tournament.name for tournament in tournament_records]
        self.news_tag_repository.save_tags(tournament_names)
