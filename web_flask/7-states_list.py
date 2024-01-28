#!/usr/bin/python3
"""Flask web application"""


from flask import Flask, render_template
from models import storage
from models import *
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ show states """
    States = storage.all(State)
    return render_template('7-states_list.html', states=States)


@app.teardown_appcontext
def tear_db(exception):
    """close storage"""
    return storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
