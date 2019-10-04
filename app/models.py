from app import db
from sqlalchemy import Table, Column, Integer, String, Date, Numeric
from sqlalchemy.dialects.postgresql import JSON#, JSONB


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(256), index=True, unique=True)
    pw_hash = Column(String(128))
    createdon = Column(Date)
    lastlogin = Column(Date)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

class UserLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    long = db.Column(db.Numeric)
    lat = db.Column(db.Numeric)
    elev = db.Column(db.Numeric)
    timestamp = db.Column(db.Date)

    def __repr__(self):
        return '<UserLocation {}>'.format(self.id)

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, index=True)
    name = db.Column(db.String(256), index=True)
    props = db.Column(db.JSON)
    registeredon = db.Column(db.Date)

    def __repr__(self):
        return '<Device {}>'.format(self.name)

class GameObject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer) # foreign key
    game = db.Column(db.JSON)

    def __repr__(self):
        return '<GameObject {}>'.format(self.id)
