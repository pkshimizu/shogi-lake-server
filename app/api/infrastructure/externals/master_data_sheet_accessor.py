from datetime import datetime

import gspread
from gspread import Spreadsheet

from app.api.domain.models import PlayerRecord, PlayerGradeRecord
from app.api.domain.repositories import MasterDataSheetRepository
from google.oauth2.service_account import Credentials


class MasterDataSheetAccessor(MasterDataSheetRepository):
    def load_grades(self) -> list[PlayerGradeRecord]:
        workbook = self.__open_workbook("MASTER_DATA_SHEET_ID")
        sheet = workbook.worksheet("段位")
        grades = []
        for record in sheet.get_all_records():
            grades.append(
                PlayerGradeRecord(
                    name=record["段位名"],
                    number=record["値"],
                    category=PlayerGradeRecord.parse_category(record["カテゴリ"]),
                )
            )
        return grades

    def load_players(self) -> list[PlayerRecord]:
        workbook = self.__open_workbook("MASTER_DATA_SHEET_ID")
        sheet = workbook.worksheet("棋士一覧")
        players = []
        for record in sheet.get_all_records():
            players.append(
                PlayerRecord(
                    name=record["氏名"],
                    number=record["棋士番号"],
                    birthday=datetime.strptime(record["生年月日"], "%Y年%m月%d日"),
                    birthplace=record["出身地"],
                    master_name=record["師匠"],
                    grade=record["段位"],
                    title=record["称号"],
                )
            )

        return players

    @staticmethod
    def __open_workbook(workbook_key: str) -> Spreadsheet:
        from app.api.config import config

        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]
        credentials = Credentials.from_service_account_file(
            config.get("GOOGLE_API_CREDENTIALS_JSON_PATH"), scopes=scopes
        )
        gc = gspread.authorize(credentials)
        return gc.open_by_key(config.get(workbook_key))
