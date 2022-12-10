from flask import Flask, Blueprint

from app.api.config import load_config
from app.api.database import setup_db
from app.api.injector import setup_injector
from app.api.presentation.commands import setup_commands

app = Flask(__name__)

load_config(app)

v1 = Blueprint("v1", __name__, url_prefix="/v1")

app.register_blueprint(v1)

setup_db(app)

setup_commands(app)

setup_injector(app)


@app.route("/")
def index():
    return "OK"
