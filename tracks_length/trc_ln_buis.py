import os
import sqlite3


def execute_query(query):
    path_2_db = os.path.join(os.getcwd(), 'example.sqlite3')
    connection = sqlite3.connect(path_2_db)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    records = cursor.fetchall()
    return records

