from injector import Module, Binder

from app.api.application.import_service import ImportService


class ApplicationServiceModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(ImportService, to=ImportService)
