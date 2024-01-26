#!/usr/bin/python3
""" Flask application """

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ say hello """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ show HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ show varible text """
    return f'C {text.replace("_", " ")}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    """ show variable text """
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>')
def check_integer(n):
    """ Show only integers """
    return (f"{n} is a number")


@app.route('/number_template/<int:n>')
def number_template(n):
    """ display number """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def even_or_odd(n):
    """ display number even or odd """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
