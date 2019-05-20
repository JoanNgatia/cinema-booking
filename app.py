from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/seats")
def home():
    return 'Hello world. Here now!'


@app.route("/seats/<id>/")
def seatsview(id):
    return 'Single seat view'


@app.route("/seats/<id>/book/")
def seatsbooking(id):
    return 'single seat booking'


if __name__ == '__main__':
    app.run()
