from src.Application.StorageRepository import StorageRepository
from src.Application.TodoRepository import TodoRepository
from src.Services.ApiService import ApiService


class App:
    def __init__(self):
        self._api_service = ApiService(TodoRepository(), StorageRepository())

    def api_service(self) -> ApiService:
        return self._api_service
