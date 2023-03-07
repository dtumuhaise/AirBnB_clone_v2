#!/usr/bin/python3
"""wsgi configuration """

from web_flask import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
