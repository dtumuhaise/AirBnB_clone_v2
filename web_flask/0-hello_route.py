#!/usr/bin/python3
""" script that starts a flask web application"""

from flask import Flask
from web_flask.0-hello_route import app

app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
