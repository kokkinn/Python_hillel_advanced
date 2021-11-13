from flask import Flask

from flask_hmWRK_6_trckLength.format3r import form7t
from flask_hmWRK_6_trckLength.trc_ln_buis import execute_query

app = Flask(__name__)


@app.route("/track_length")
def view():
    sql = execute_query("SELECT GenreID, Milliseconds FROM tracks")
    sql2 = execute_query("SELECT GenreID, Name FROM genres")

    return form7t(sql, sql2)


app.run(debug=True)
