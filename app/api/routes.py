from flask import Flask, Blueprint

from app.api.presentation.controllers.news_controller import news_module


def setup_routes(app: Flask):
    v1 = Blueprint("v1", __name__, url_prefix="/v1")

    v1.register_blueprint(news_module)

    app.register_blueprint(v1)
