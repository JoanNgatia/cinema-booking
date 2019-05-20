from app import db
from sqlalchemy.dialects.postgresql import JSON


class Seat(db.Model):
    __tablename__ = 'seats'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    booked = db.Boolean()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    email = db.Column(db.String(10))
    phone_number = db.Column(db.String(10))
