from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def setup_db(app: Flask):
    db.init_app(app)
    from app.api.infrastructure.datasources import entities

    Migrate(app, db)
