import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)


@app.route("/")
@app.route("/seats")
def home():
    return render_template('home.html')


@app.route("/seats/<id>/")
def seatsview(id):
    return 'Single seat view'


@app.route("/seats/<id>/book/")
def seatsbooking(id):
    return 'single seat booking'


if __name__ == '__main__':
    app.run()
