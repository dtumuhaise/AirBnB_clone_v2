#!/usr/bin/python3
"""  script that starts a Flask web application:"""

from flask import Flask

app = Flask(__name__)
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
