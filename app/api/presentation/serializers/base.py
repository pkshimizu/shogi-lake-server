from dataclasses import dataclass, asdict
from datetime import datetime

from flask import request


@dataclass
class Request:
    def __init__(self):
        self.request = request

    def get_str(self, name: str):
        return self.request.json.get(name)


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
