import sqlite3
from abc import abstractmethod, ABC
import os

class Db_api():
    def __init__(self, db_name):
        server_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(server_dir)
        db_path = os.path.join(parent_dir, "db", "your_database.db")
        self.db_name = db_name
        self.path = db_path
    def init_db(self):
        connection = sqlite3.connect(self.path )
        cursor = connection.cursor()

        # Создаем таблицу Users
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Worker (
        id INTEGER PRIMARY KEY,
        patronymic TEXT NOT NULL,
        name TEXT NOT NULL,
        lastname TEXT NOT NULL,
        number INTEGER
        )
        ''')

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS WorkerShift (
                id INTEGER PRIMARY KEY,
                worker TEXT NOT NULL,
                date TEXT NOT NULL,
                timeStartWork TEXT NOT NULL,
                timeEndWork TEXT NOT NULL,
                FOREIGN KEY (worker) REFERENCES Worker (id)
                )
                ''')

        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS WorkerShift (
                        id INTEGER PRIMARY KEY,
                        worker TEXT NOT NULL,
                        date TEXT NOT NULL,
                        timeStartWork TEXT NOT NULL,
                        timeEndWork TEXT NOT NULL,
                        FOREIGN KEY (worker) REFERENCES Worker (id)
                        )
                        ''')

        cursor.execute('''
                                CREATE TABLE IF NOT EXISTS WorkerShift (
                                id INTEGER PRIMARY KEY,
                                worker TEXT NOT NULL,
                                date TEXT NOT NULL,
                                timeStartWork TEXT NOT NULL,
                                timeEndWork TEXT NOT NULL,
                                FOREIGN KEY (worker) REFERENCES Worker (id)
                                )
                                ''')

        # Сохраняем изменения и закрываем соединение
        connection.commit()
        connection.close()
        return True
if __name__ == "__main__":
    db = Db_api
    db.init_db()