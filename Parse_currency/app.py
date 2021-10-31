from flask import Flask
from webargs import fields
from webargs.flaskparser import use_kwargs
from util import f1nd

app = Flask(__name__)


@app.route("/")
@use_kwargs({"currency": fields.Str(missing="USD")}, location='query')
def get_cur(currency):
    return "<h1>" + f'{f1nd(currency)}' + "</h1>"


app.run(debug=True)

# вы не говорили проверять но тем не менее, как тут лучше обработать некоректное значение? была идея у меня с помощью validate
# сравнивать со списком кодов валют 
