from flask import Flask
app = Flask(__name__)
""" Flask application """


@app.route('/', strict_slashes=False)
def hello():
    """ say hello """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
