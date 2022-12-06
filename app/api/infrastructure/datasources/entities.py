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
