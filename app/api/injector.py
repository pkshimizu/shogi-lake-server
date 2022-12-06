from injector import Injector

from app.api.application import ApplicationServiceModule
from app.api.infrastructure.datasources import DatasourceModule
from app.api.infrastructure.externals import ExternalModule

injector = Injector([ApplicationServiceModule(), DatasourceModule(), ExternalModule()])
