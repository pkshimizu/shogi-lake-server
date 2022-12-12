from injector import inject

from app.api.application.decorators import transaction
from app.api.domain.repositories import (
    MasterDataSheetRepository,
    PlayerRepository,
    PlayerGradeRepository,
)


class ImportService:
    @inject
    def __init__(
        self,
        master_data_sheet_repository: MasterDataSheetRepository,
        player_grade_repository: PlayerGradeRepository,
        player_repository: PlayerRepository,
    ):
        self.master_data_sheet_repository = master_data_sheet_repository
        self.player_grade_repository = player_grade_repository
        self.player_repository = player_repository

    @transaction
    def import_player_grade(self) -> None:
        grade_records = self.master_data_sheet_repository.load_grades()
        self.player_grade_repository.save_from_records(grade_records)

    @transaction
    def import_player(self) -> None:
        player_records = self.master_data_sheet_repository.load_players()
        self.player_repository.save_from_records(player_records)
