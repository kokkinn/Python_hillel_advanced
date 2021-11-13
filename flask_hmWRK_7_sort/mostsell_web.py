from flask import Flask
from webargs import fields
from webargs.flaskparser import use_kwargs

from flask_hmWRK_7_sort.conn import execute_query
from flask_hmWRK_7_sort.mostsell_buis import formatR

app = Flask(__name__)


@app.route("/count")
@use_kwargs({"num": fields.Int(required=False, validate=\
    lambda x: 0 <= x <= len(execute_query("select trackid, unitprice, quantity from invoice_items")))}, location="query")
def countt(num=None):
    sql1 = execute_query("select Trackid, Name from tracks")
    sql2 = execute_query("select trackid, unitprice, quantity from invoice_items")
    a = formatR(sql1, sql2, num)
    return a


app.run(debug=True)
