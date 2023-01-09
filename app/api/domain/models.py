from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, date
from enum import IntEnum
from typing import Generic, TypeVar

from dateutil.relativedelta import relativedelta


class PlayerGradeCategory(IntEnum):
    pro = 1
    woman = 2
    amateur = 3


T = TypeVar("T")


@dataclass
class Pagination(Generic[T]):
    items: list[T]
    page: int
    next_page: int | None
    prev_page: int | None
    per_page: int
    total: int

    @staticmethod
    def to_model(items: list[T], paginate):
        return Pagination(
            items=items,
            page=paginate.page,
            next_page=paginate.next_num if paginate.has_next else None,
            prev_page=paginate.prev_num if paginate.has_prev else None,
            per_page=paginate.per_page,
            total=paginate.total,
        )


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


@dataclass
class NewsProvider:
    SHOGI_FEDERATION_UID = "NQGm4DJ8cvUj5cdMDz7mst"
    YOMIURI_NEWS_UID = "epcBcsWbRRvJhppsDhVGJ7"
    ASAHI_NEWS_UID = "fA6h5aA9wF8U4M5c2TwRNB"
    MAINICHI_NEWS_UID = "T3xP2k4s6HGeaUN6oGxcaN"
    HOKKAIDO_NEWS_UID = "matpnAvrde8EFXVXm4oxZs"

    uid: str
    name: str
    rss_url: str


@dataclass
class News:
    id: int
    uid: str
    url: str
    image_url: str
    title: str
    published_at: datetime
    provider: NewsProvider
    tags: list[NewsTag]


@dataclass
class NewsTag:
    uid: str
    name: str


@dataclass
class NewsEntry:
    def __init__(self, url: str, title: str, published_at: str, provider_uid: str):
        self.url = self.convert_url(url)
        self.title = self.convert_title(title)
        self.published_at = self.convert_published_at(published_at)
        self.provider_uid = provider_uid

    url: str
    title: str
    published_at: datetime
    provider_uid: str

    @staticmethod
    def convert_url(url: str) -> str:
        return url

    @staticmethod
    def convert_title(title: str) -> str:
        return title

    @staticmethod
    def convert_published_at(published_at: str | datetime) -> datetime:
        if type(published_at) is datetime:
            return published_at
        return datetime.strptime(published_at, "%Y/%m/%d %H:%M")


class MainichiNewsEntry(NewsEntry):
    @staticmethod
    def convert_url(url: str) -> str:
        return f"https:{url}"

    @staticmethod
    def convert_published_at(published_at: str) -> datetime:
        return datetime.strptime(published_at, "%Y/%m/%d %H:%M")


class HokkaidoNewsEntry(NewsEntry):
    @staticmethod
    def convert_url(url: str) -> str:
        return f"https://www.hokkaido-np.co.jp{url}"

    @staticmethod
    def convert_published_at(text: str) -> datetime:
        today = datetime.today()
        text = f"{today.year}/{text}"
        if "更新" in text:
            published_at = datetime.strptime(text, "%Y/%m/%d %H:%M 更新")
        else:
            published_at = datetime.strptime(text, "%Y/%m/%d %H:%M")
        if published_at > today:
            published_at = published_at - relativedelta(years=1)
        return published_at
