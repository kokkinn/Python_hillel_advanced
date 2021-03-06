from flask import Flask
from webargs import fields
from webargs.flaskparser import use_kwargs
from parse_cur_buisines import f1nd

app = Flask(__name__)


@app.route("/")
@use_kwargs({"currency": fields.Str(missing="USD")}, location='query')
def get_cur(currency):
    return "<h1>" + f'{f1nd(currency)}' + "</h1>"


app.run(debug=True)

