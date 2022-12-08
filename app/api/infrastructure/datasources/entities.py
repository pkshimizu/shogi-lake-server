from datetime import datetime

import shortuuid

from app.api.database import db


class BaseEntity:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )
    deleted_at = db.Column(db.DateTime)


def generate_uid():
    return shortuuid.uuid()


class UidEntity(BaseEntity):
    uid = db.Column(db.String(32), default=generate_uid)


class Player(UidEntity):
    name = db.Column(db.String)
    number = db.Column(db.Integer)
    grade = db.Column(db.Integer)
    birthday = db.Column(db.Date)
    birthplace = db.Column(db.String)
    master_id = db.Column(db.Integer)


class Tournament(UidEntity):
    name = db.Column(db.String)
    term = db.Column(db.Integer)
    title_holder_player_id = db.Column(db.Integer)


class Game(UidEntity):
    tournament_id = db.Column(db.Integer)
    date = db.Column(db.Date)
    player1_id = db.Column(db.Integer)
    player2_id = db.Column(db.Integer)
    result = db.Column(db.Integer)


class NewsProvider(UidEntity):
    name = db.Column(db.String)


class News(UidEntity):
    url = db.Column(db.String)
    news_provider_id = db.Column(db.Integer)


class NewsTag(UidEntity):
    news_id = db.Column(db.Integer)
    name = db.Column(db.String)
