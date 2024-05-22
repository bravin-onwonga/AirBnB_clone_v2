#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Simple flask setup to display Hello HBNB
    """
    return ("Hello HBNB")

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
