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


class PlayerEntity(db.Model, UidEntity):
    __tablename__ = "player"

    name = db.Column(db.String(16), nullable=False)
    number = db.Column(db.Integer)
    grade_id = db.Column(db.Integer, db.ForeignKey("player_grade.id"))
    grade = db.relationship("PlayerGradeEntity", lazy="joined", innerjoin=True)
    title = db.Column(db.String(16))
    birthday = db.Column(db.Date, nullable=False)
    birthplace = db.Column(db.String(16), nullable=False)
    master_id = db.Column(db.Integer, db.ForeignKey("player.id"))


class PlayerGradeEntity(db.Model, BaseEntity):
    __tablename__ = "player_grade"

    name = db.Column(db.String(16), nullable=False)
    number = db.Column(db.Integer)
    category = db.Column(db.Integer)
    players = db.relationship("PlayerEntity", back_populates="grade")


class TournamentEntity(db.Model, UidEntity):
    __tablename__ = "tournament"

    name = db.Column(db.String(32), nullable=False)
    terms = db.relationship("TournamentTermEntity", back_populates="tournament")


class TournamentTermEntity(db.Model, UidEntity):
    __tablename__ = "tournament_term"

    tournament_id = db.Column(db.Integer, db.ForeignKey("tournament.id"))
    tournament = db.relationship("TournamentEntity", back_populates="terms")
    term = db.Column(db.Integer, nullable=False)
    title_holder_player_id = db.Column(db.Integer)


class GameEntity(db.Model, UidEntity):
    __tablename__ = "game"

    tournament_id = db.Column(db.Integer)
    date = db.Column(db.Date, nullable=False)
    player1_id = db.Column(db.Integer, nullable=False)
    player2_id = db.Column(db.Integer, nullable=False)
    result = db.Column(db.Integer, nullable=False)


class NewsProviderEntity(db.Model, UidEntity):
    __tablename__ = "news_provider"

    name = db.Column(db.String(16), nullable=False)


class NewsEntity(db.Model, UidEntity):
    __tablename__ = "news"

    url = db.Column(db.String(256), nullable=False)
    news_provider_id = db.Column(
        db.Integer, db.ForeignKey("news_provider.id"), nullable=False
    )
    news_provider = db.relationship("NewsProviderEntity", lazy="joined", innerjoin=True)
    news_tags = db.relationship("NewsTagEntity", lazy="joined", innerjoin=True)


class NewsTagEntity(db.Model, UidEntity):
    __tablename__ = "news_tag"

    news_id = db.Column(db.Integer, db.ForeignKey("news.id"), nullable=False)
    news_list = db.relationship("NewsEntity", back_populates="news_tags")
    name = db.Column(db.String(32), nullable=False)
