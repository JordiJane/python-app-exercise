
import unittest
from unittest.mock import MagicMock
from src.Services.ApiService import ApiService
from src.Application.TodoRepository import TodoRepository
from src.Application.StorageRepository import StorageRepository

class ApiServiceTest(unittest.TestCase):
    def test_storage_should_save_todo_repository_result(self):
        #Given
        todo_repository = TodoRepository()
        todo_repository.getTodos = MagicMock(return_value=
        '''
            [
                {
                    "userId": 1,
                    "id": 1,
                    "title": "delectus aut autem",
                    "completed": false
                },
            ]
        ''')
        storage_repository = StorageRepository()
        storage_repository.save = MagicMock()
        api_service = ApiService(todo_repository, storage_repository)

        #When
        api_service.run()

        #Then
        storage_repository.save.assert_called_with('''
            [
                {
                    "userId": 1,
                    "id": 1,
                    "title": "delectus aut autem",
                    "completed": false
                },
            ]
        ''')

if __name__ == '__main__':
    unittest.main()