import sqlite3
import os


def get_data(query):
    path = os.path.join(os.getcwd(), "example.sqlite3")
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    records = cursor.fetchall()
    return records

