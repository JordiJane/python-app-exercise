# Python App Exercise

## Solution Decisions
- Logic to retrieve todos from the API is inside of TodoRepository.py
- Logic to save todos into storage is inside of StorageRepository.py
- The dependencies of API service are injected into App.py
- Logic from ApiService is unit tested into test_ApiService.py (mocking his dependencies). 
- The tests are executed with:

    ```
    python -m unittest
    ```

## Exercise
- Use the ApiService to fetch TODOs from an API and save them into the _storage_ folder
    - TODOs can be accessed from this URL: https://jsonplaceholder.typicode.com/todos/
    - Each TODO should be saved on a single file in CSV format
    - The filename must contain the TODO "id" prefixed with the current date.
        - Example: 2021_04_28_123.csv


## Extra points
- Use _requests_ library from [PyPI](https://pypi.org/project/requests/)

