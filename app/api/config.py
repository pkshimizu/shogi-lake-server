from flask import Flask


def load_config(app: Flask):
    app.config.from_object("app.api.env.local")
