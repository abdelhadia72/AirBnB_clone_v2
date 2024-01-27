#!/usr/bin/python3
""" Flask application """

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(self):
    """ close storage """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """ display page """
    states = storage.all('State').values()
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
