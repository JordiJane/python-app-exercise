from sys import stderr
from src.Application.TodoRepository import TodoRepository
from src.Application.StorageRepository import StorageRepository

class ApiService:
    def __init__(self, todo_repository : TodoRepository, storage_repository : StorageRepository):
        self.todo_repository = todo_repository
        self.storage_repository = storage_repository

    def run(self):
        print('Running ApiService', file=stderr)
        print('Reading Todos', file=stderr)
        todos = self.todo_repository.getTodos()
        print('Writing Todos into storage', file=stderr)
        self.storage_repository.save(todos)
