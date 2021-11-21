from flask import Flask

from flask_hmWRK_6_trckLength.track_len_formater import form7t
from flask_hmWRK_6_trckLength.trc_len_con import execute_query

app = Flask(__name__)


@app.route("/track_length")
def view():
    sql2 = execute_query("SELECT GenreID, Name FROM genres")

    return form7t(sql2)


app.run(debug=True)
