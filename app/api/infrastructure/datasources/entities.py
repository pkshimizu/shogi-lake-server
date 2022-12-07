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
    birthday = db.Column(db.Date)
    birthplace = db.Column(db.String)
    master_id = db.Column(db.Integer)


class Tournament(UidEntity):
    name = db.Column(db.String)


class Game(UidEntity):
    tournament_id = db.Column(db.Integer)
    player1_id = db.Column(db.Integer)
    player2_id = db.Column(db.Integer)
    result = db.Column(db.Integer)


class News(UidEntity):
    pass
