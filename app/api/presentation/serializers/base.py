from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Generic, TypeVar

from flask import request

from app.api.domain.models import Pagination


@dataclass
class Request:
    def __init__(self):
        self.request = request

    def get_str(self, name: str):
        return self.request.json.get(name)

    def get_query_int(self, name: str, default: int = None) -> int:
        return int(self.request.args.get(name, default=default))


@dataclass
class Resource:
    @staticmethod
    def datetime_str(value: datetime | None) -> str | None:
        if value is None:
            return None

        return value.isoformat()


@dataclass
class Response(Resource):
    def __init__(self, status_code: int):
        self.status_code = status_code

    def data(self):
        return asdict(self), self.status_code


@dataclass
class MessageResponse(Response):
    def __init__(self, message: str, status_code: int = 200):
        super().__init__(status_code)
        self.message = message

    message: str


@dataclass
class ErrorResponse(Response):
    def __init__(self, message: str, status_code: int):
        super().__init__(status_code)
        self.message = message

    message: str


T = TypeVar("T")


@dataclass
class PaginationResponse(Response, Generic[T]):
    def __init__(self, items: list[T], pagination: Pagination, status_code: int):
        super().__init__(status_code)
        self.items = items
        self.page = pagination.page
        self.next_page = pagination.next_page
        self.prev_page = pagination.prev_page
        self.per_page = pagination.per_page
        self.total = pagination.total

    items: list[T]
    page: int
    next_page: int | None
    prev_page: int | None
    per_page: int
    total: int
