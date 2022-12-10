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
