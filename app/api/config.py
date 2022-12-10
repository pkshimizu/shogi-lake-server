from flask import Flask, Config

config: Config


def load_config(app: Flask):
    app.config.from_object("app.api.env.local")
    global config
    config = app.config
