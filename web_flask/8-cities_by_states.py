#!/usr/bin/python3
"""Falsk application"""


from flask import Flask, render_template
from models import *
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ display states and cities"""

    States = storage.all(State)

    return render_template("8-cities_by_states.html", states=States)


@app.teardown_appcontext
def tear(e):
    """ close storage """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
