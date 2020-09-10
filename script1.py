from flask import Flask
# imported the "Flask" object from flask library
app = Flask(__name__)


@app.route('/')
def home():
    return "This is the playground to create"


if __name__ == "__main__":
    app.run(debug=True)
