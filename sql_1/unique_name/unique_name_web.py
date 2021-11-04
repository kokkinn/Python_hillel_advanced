from flask import Flask

from sql_1.unique_name.formater import rec2html
from u_n_buisiness import execute_query

app = Flask(__name__)


@app.route('/unique_name')
def qe():
    sql = 'SELECT FirstName FROM customers GROUP BY FirstName'
    record = execute_query(sql)
    return rec2html(record)


app.run(debug=True)
