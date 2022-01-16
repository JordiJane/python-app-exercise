import requests
import json


class TodoRepository:

    def __init__(self):
        self.url = "https://jsonplaceholder.typicode.com/todos/"

    def getTodos(self):
        r = requests.get(self.url)
        todos = json.loads(r.content)
        r.close()
        return todos
