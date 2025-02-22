#!/usr/bin/python3
""" script that starts a flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(port=5000)
