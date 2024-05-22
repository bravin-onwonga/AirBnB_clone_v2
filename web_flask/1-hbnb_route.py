#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Simple route display Hello HBNB
    """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Simple route to display HBNB
    """
    return ("HBNB")


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
