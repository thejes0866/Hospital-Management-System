from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(150))
    phno = db.Column(db.Integer)
    first_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    comments = db.relationship('PatientComments')
    appointments = db.relationship('AppointmentBooking')



class Doctor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    doc_id = db.Column(db.Integer, unique=True)
    domain = db.Column(db.String(150))
    phno = db.Column(db.Integer)
    first_name = db.Column(db.String(150))
    specialization = db.Column(db.String(150))
    day = db.Column(db.String(150))
    slot = db.Column(db.String(150))
    password = db.Column(db.String(150)) 
    varified = db.Column((db.String(150)), default='False')



class PatientComments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), db.ForeignKey('user.email'))
    comments = db.Column(db.String(250))
    reply = db.Column(db.String(250))
    domain = db.Column(db.String(50))
    checked = db.Column((db.String(150)), default='False')

class AppointmentBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), db.ForeignKey('user.email'))
    doctor = db.Column(db.String(150))
    domain = db.Column(db.String(50))
    day = db.Column(db.String(150))
    slot = db.Column(db.String(150))
    status = db.Column(db.String(150), default='True')

