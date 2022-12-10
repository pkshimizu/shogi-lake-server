from injector import inject

from app.api.domain.repositories import MasterDataSheetRepository


class ImportService:
    @inject
    def __init__(self, master_data_sheet_repository: MasterDataSheetRepository):
        self.master_data_sheet_repository = master_data_sheet_repository

    def import_player(self) -> None:
        players = self.master_data_sheet_repository.load_players()
        print(players)
