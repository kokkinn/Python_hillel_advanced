from flask import Flask

from tracks_length.format3r import form7t
from tracks_length.trc_ln_buis import execute_query

app = Flask(__name__)


@app.route("/track_length")
def view():
    sql2 = execute_query("SELECT GenreID, Name FROM genres")

    return form7t(sql2)


app.run(debug=True)
