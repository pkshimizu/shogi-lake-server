from flask import Flask
from flask_injector import FlaskInjector
from injector import Injector

from app.api.application import ApplicationServiceModule
from app.api.infrastructure.datasources import DatasourceModule
from app.api.infrastructure.externals import ExternalModule

injector: Injector = None


def setup_injector(app: Flask):
    global injector
    flask_injector = FlaskInjector(
        app=app, modules=[DatasourceModule, ExternalModule, ApplicationServiceModule]
    )
    injector = flask_injector.injector
