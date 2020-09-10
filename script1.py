from flask import Flask, render_template
# imported the "Flask" object from flask library
app = Flask(__name__)


@app.route('/')
# @app.route('/about/')
# app.route() is a decorator
def home():
    # return "the main reception"
    return render_template("home.html")


@app.route('/about/')
def about():
    # return "This is the playground to create"
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
