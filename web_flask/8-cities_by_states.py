#!/usr/bin/python3
""" flast application """

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
@app.route('/cities_by_states/<state_id>', strict_slashes=False)
def cities_by_states(state_id=None):
    """ Display states and cities """
    if state_id:
        state = storage.get("State", state_id)
        if state:
            cities = state.cities
            return render_template(
                '8-cities_by_states.html',
                state=state,
                cities=cities)

    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ Closes storage """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
