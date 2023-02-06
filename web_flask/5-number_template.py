#!/usr/bin/python3
"""  script that starts a Flask web application:"""

from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="templates/")
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def fun(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python/<text>")
@app.route("/python/", defaults={'text': 'is cool'})
def python(text):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def num(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def html(n):
    return render_template("5-number.html", n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
