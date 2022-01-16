from datetime import datetime
import csv
import os


class StorageRepository:

    PATH = 'storage/'

    def save(self, todos):
        for i in range(len(todos)):
            user_id = todos[i]["userId"]
            id = todos[i]["id"]
            title = todos[i]["title"]
            completed = todos[i]["completed"]
            file_name = datetime.today().strftime('%Y_%m_%d') + "_" + str(todos[i]["id"]) + ".csv"

            with open(os.path.join(self.PATH, file_name), 'w', newline='') as file:
                writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=';')
                writer.writerow(todos[i])
                writer.writerow([user_id, id, title, completed])
