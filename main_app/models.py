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
    imei = db.Column(db.String(20))
    currentDateTime = db.Column(db.DateTime)
    gpsDateTime = db.Column(db.DateTime)
    Datatype = db.Column(db.Integer)
    address = db.Column(db.String(1000))
    distance = db.Column(db.Integer)

    def __init__(self, name, code, default, active):
        self.imei = imei
        self.currentDateTime = currentDateTime
        self.gpsDateTime = gpsDateTime
        self.Datatype = Datatype
        self.address = address
        self.distance = distance

    def __repr__(self):
        return self.imei