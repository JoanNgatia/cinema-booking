from app import db


class Seat(db.Model):
    __tablename__ = 'seats'

    id = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(10))
    booked = db.Boolean()

    def __repr__(self):
        return '<id {}>'.format(self.id)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    email = db.Column(db.String(10))
    phone_number = db.Column(db.String(10))

    def __repr__(self):
        return '<name {}>'.format(self.name)