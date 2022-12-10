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
    def parse(text: str) -> PlayerGradeRecord:
        dan_list = ["初段", "二段", "三段", "四段", "五段", "六段", "七段", "八段", "九段"]
        if text in dan_list:
            num = dan_list.index(text)
            return PlayerGradeRecord(
                name=text, number=num + 1, category=PlayerGradeCategory.pro
            )
        raise Exception


@dataclass
class PlayerRecord:
    name: str
    number: int
    birthday: date
    birthplace: str
    master_name: str
    grade: PlayerGradeRecord
    title: str
