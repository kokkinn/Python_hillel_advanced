from flask import Flask
from faker import Faker

qw = Flask(__name__)


@qw.route("/get_requirements")
def reqs():
    file = open("requirements.txt", "r")
    l1st = []
    for i in file:
        l1st.append(i)
    file.close()
    return '<p>' + '<br>'.join(l1st) + '<p>'


@qw.route("/avr_data")
def get_avg_data():
    file = open("hw-1.csv", encoding="UTF8")
    next(file)
    weight = 0
    height = 0
    count = 0
    for line in file:
        b = line.split(", ")
        b = [float(i) for i in b]
        count += 1
        weight += b[2]
        height += b[1]
    file.close()
    return (f"<h1>The average weight is {round(weight / count * 0.45359237, 1)} kg \
            <br>The average height is {round((height / count * 2.54), 1)} cm</h1>")


@qw.route("/get_random_students")
def random():
    l1st = []
    fake = Faker()
    for _ in range(100):
        l1st.append(fake.name())
    return '<p>' + '<br>'.join(l1st) + '<p>'


qw.run(debug=True)
