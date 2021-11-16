from flask import Flask
from webargs import fields
from webargs.flaskparser import use_kwargs

from flask_hmWRK_8_joinSQL.connection import execute_query

app = Flask(__name__)


@app.route("/tracklen")
def track_len():
    sql = execute_query("SELECT g.Name, SUM(t.Milliseconds)/1000 from tracks t join genres g on"
                        " t.GenreId = g.GenreId GROUP by g.GenreId")
    return '<br>'.join(map(lambda x: str(x[0]) + ' ' + str(x[1]), sql))


@app.route("/track_sort")
@use_kwargs({"num": fields.Int(required=False, validate= \
        lambda x: 0 <= x <= len(execute_query("select trackid, unitprice, quantity from invoice_items")))},
            location="query")
def track_sort(num=None):
    sql = execute_query("SELECT Name, ii.UnitPrice * ii.Quantity as Sum_of_sells, ii.Quantity from tracks t join "
                        "invoice_items ii ON t.TrackId = ii.TrackId order by ii.Quantity")
    sql = sql[:num]
    return '<br>'.join(map(lambda x: str(x[0]) + ' ' + str(x[1]) + " " + str(x[2]), sql))


app.run(debug=True)
