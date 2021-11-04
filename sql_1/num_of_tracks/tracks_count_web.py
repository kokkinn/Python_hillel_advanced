from flask import Flask

from sql_1.num_of_tracks.format import formatt
from sql_1.num_of_tracks.tracks_count_buisiness import get_data

app = Flask(__name__)


@app.route('/tracks_count')
def count():
    sql = "SELECT COUNT() FROM tracks"
    record = get_data(sql)
    return formatt(record)


app.run(debug=True)
