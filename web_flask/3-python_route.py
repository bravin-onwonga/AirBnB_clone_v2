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


@app.route("/c/<text>", strict_slashes=False)
def route_vars(text):
    """
    Simple route that accepts a string
    Returns:
        string with _ instead of space
    """
    text = text.replace('_', ' ')
    return ("C {}".format(text))


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def route_python(text):
    """
    Simple route that accepts a string
    Returns:
        string with _ instead of space
    """
    text = text.replace('_', ' ')
    return ("Python {}".format(text))


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
