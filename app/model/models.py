# app/model/models.py

from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Songs(db.Model):
    __tablename__ = "Songs"
    id = db.Column(db.BigInteger, primary_key=True)
    genre = db.Column(db.String(50))
    artist_name = db.Column(db.String(50))
    track_name = db.Column(db.String(100))
    track_id = db.Column(db.String(50))
    popularity = db.Column(db.Integer)
    acousticness = db.Column(db.Float)
    danceability = db.Column(db.Float)
    duration_ms = db.Column(db.Integer)
    energy = db.Column(db.Float)
    instrumentalness = db.Column(db.Float)
    key = db.Column(db.Integer)
    liveness = db.Column(db.Float)
    loudness = db.Column(db.Float)
    mode = db.Column(db.Integer)
    speechiness = db.Column(db.Float)
    tempo = db.Column(db.Float)
    time_signature = db.Column(db.Integer)
    valence = db.Column(db.Float)

    def __repr__(self):
        return '<Song {}>'.format(self.track_name)
