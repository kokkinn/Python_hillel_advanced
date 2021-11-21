import os
import sqlite3

def execute_query(query):
    path2db = os.path.join(os.getcwd(), "example.sqlite3")
    connection = sqlite3.connect(path2db)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    res = cursor.fetchall()
    return res
