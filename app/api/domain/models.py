from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, date
from enum import IntEnum


class PlayerGradeCategory(IntEnum):
    pro = 1
    woman = 2
    amateur = 3


@dataclass
class PlayerGrade:
    id: int
    created_at: datetime
    updated_at: datetime
    name: str
    number: int
    category: PlayerGradeCategory


@dataclass
class Player:
    id: int
    uid: str
    created_at: datetime
    updated_at: datetime
    name: str
    number: int
    birthday: date
    birthplace: str
    master: Player
    grade: PlayerGrade
    title: str


@dataclass
class PlayerGradeRecord:
    name: str
    number: int
    category: PlayerGradeCategory

    @staticmethod
    def parse_category(text: str) -> PlayerGradeCategory:
        if text == "棋士":
            return PlayerGradeCategory.pro
        if text == "女流棋士":
            return PlayerGradeCategory.woman
        if text == "アマチュア":
            return PlayerGradeCategory.amateur
        raise Exception


@dataclass
class PlayerRecord:
    name: str
    number: int
    birthday: date
    birthplace: str
    master_name: str
    grade: str
    title: str


@dataclass
class TournamentTermRecord:
    name: str
    is_official: bool
    term: int
    title_holder_player_name: str
