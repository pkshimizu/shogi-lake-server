from flask import Blueprint
from injector import inject

news_module = Blueprint("news", __name__, url_prefix="/news")


@news_module.route("")
@inject
def get_list():
    pass
