from flask import Flask
# imported the "Flask" object from flask library
app = Flask(__name__)


@app.route('/')
# @app.route('/about/')
# app.route() is a decorator
def home():
    return "the main reception"


@app.route('/about/')
def about():
    return "This is the playground to create"


if __name__ == "__main__":
    app.run(debug=True)
