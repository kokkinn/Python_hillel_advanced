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


app.run(debug=True)
