import sqlite3
from sqlite3 import Error


def create_connection(path):  # Определяет функцию , которая принимает путь к базе данных SQLite.
    connection = None  # Использует метод и принимает в качестве параметра путь к базе данных SQLite.
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")  # Вывод успешного подключения
    except Error as e:
        print(f"The error '{e}' occurred")  # Ошибка

    return connection


connection = create_connection("E:\\sm_app.sqlite")
