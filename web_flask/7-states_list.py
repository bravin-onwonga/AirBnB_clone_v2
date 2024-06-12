#!/usr/bin/python3
"""Starts a Flask application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close(Exception):
    """Removes the current sqlalchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """Displays an HTML page"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
