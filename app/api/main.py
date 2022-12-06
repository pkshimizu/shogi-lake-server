from flask import Flask, Blueprint

app = Flask(__name__)

v1 = Blueprint("v1", __name__, url_prefix="/v1")

app.register_blueprint(v1)


@app.route("/")
def index():
    return "OK"
