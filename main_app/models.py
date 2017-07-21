from main_app import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app.config.update(
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(APP_ROOT, 'data.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS=True
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Imei = db.Column(db.String(20))
    CurrentDateTime = db.Column(db.DateTime)
    GPSDateTime = db.Column(db.DateTime)
    Datatype = db.Column(db.Integer)
    Address = db.Column(db.String(1000))
    Distance = db.Column(db.Integer)

    def __init__(self, Imei, CurrentDateTime, GPSDateTime, Datatype, Address, Distance):
        self.Imei = Imei
        self.CurrentDateTime = CurrentDateTime
        self.GPSDateTime = GPSDateTime
        self.Datatype = Datatype
        self.Address = Address
        self.Distance = Distance

    def __repr__(self):
        return self.Imei