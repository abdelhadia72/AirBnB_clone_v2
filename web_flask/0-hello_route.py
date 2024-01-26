from flask import Flask
app = Flask(__name__)
""" Flask application """


@app.route('/')
def hello():
    """ say hello """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
