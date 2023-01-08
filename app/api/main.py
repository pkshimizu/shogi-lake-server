from flask import Flask

from app.api.config import load_config
from app.api.database import setup_db
from app.api.injector import setup_injector
from app.api.presentation.commands import setup_commands
from app.api.routes import setup_routes

app = Flask(__name__)

load_config(app)

setup_routes(app)

setup_db(app)

setup_commands(app)

setup_injector(app)


@app.route("/")
def index():
    return "OK"
