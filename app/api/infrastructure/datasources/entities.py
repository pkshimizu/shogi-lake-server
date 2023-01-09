from datetime import datetime

import shortuuid

from app.api.database import db
from app.api.domain.models import (
    News,
    NewsProvider,
    NewsTag,
    Player,
    PlayerGrade,
)


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

    def to_model(self) -> Player:
        return Player(
            id=self.id,
            uid=self.uid,
            created_at=self.created_at,
            updated_at=self.updated_at,
            name=self.name,
            number=self.number,
            birthday=self.birthday,
            birthplace=self.birthplace,
            grade=self.grade.to_model(),
            title=self.title,
        )


class PlayerGradeEntity(db.Model, BaseEntity):
    __tablename__ = "player_grade"

    name = db.Column(db.String(16), nullable=False)
    number = db.Column(db.Integer)
    category = db.Column(db.Integer)
    players = db.relationship("PlayerEntity", back_populates="grade")

    def to_model(self):
        return PlayerGrade(
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            name=self.name,
            number=self.number,
            category=self.category.to_model(),
        )


class TournamentEntity(db.Model, UidEntity):
    __tablename__ = "tournament"

    name = db.Column(db.String(32), nullable=False)
    terms = db.relationship("TournamentTermEntity", back_populates="tournament")
    is_official = db.Column(db.Boolean)


class TournamentTermEntity(db.Model, UidEntity):
    __tablename__ = "tournament_term"

    tournament_id = db.Column(db.Integer, db.ForeignKey("tournament.id"))
    tournament = db.relationship(
        "TournamentEntity", back_populates="terms", lazy="joined", innerjoin=True
    )
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
    rss_url = db.Column(db.String(256), nullable=True)

    def to_model(self):
        return NewsProvider(uid=self.uid, name=self.name, rss_url=self.rss_url)


news_news_tag_table = db.Table(
    "news_news_tag",
    db.metadata,
    db.Column("news_id", db.Integer, db.ForeignKey("news.id")),
    db.Column("news_tag_id", db.Integer, db.ForeignKey("news_tag.id")),
)


class NewsEntity(db.Model, UidEntity):
    __tablename__ = "news"

    title = db.Column(db.String(256), nullable=False)
    url = db.Column(db.String(256), nullable=False)
    image_url = db.Column(db.String(256), nullable=True)
    news_provider_id = db.Column(
        db.Integer, db.ForeignKey("news_provider.id"), nullable=False
    )
    news_provider = db.relationship("NewsProviderEntity", lazy="joined", innerjoin=True)
    news_tags = db.relationship(
        "NewsTagEntity", secondary=news_news_tag_table, back_populates="news_list"
    )
    published_at = db.Column(db.DateTime, nullable=False)

    def to_model(self):
        return News(
            id=self.id,
            uid=self.uid,
            url=self.url,
            image_url=self.image_url,
            title=self.title,
            published_at=self.published_at,
            provider=self.news_provider.to_model(),
            tags=[tag.to_model() for tag in self.news_tags],
        )


class NewsTagEntity(db.Model, UidEntity):
    __tablename__ = "news_tag"

    news_list = db.relationship(
        "NewsEntity", secondary=news_news_tag_table, back_populates="news_tags"
    )
    name = db.Column(db.String(32), nullable=False)

    def to_model(self):
        return NewsTag(uid=self.uid, name=self.name)
