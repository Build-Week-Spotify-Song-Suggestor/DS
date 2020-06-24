from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

class Songs(db.Model):
    __tablename__ = "Songs"
    id = db.Column(db.BigInteger, primary_key=True)
    genre = db.Column(db.String(50))
    artist_name = db.Column(db.String(50))
    track_name = db.Column(db.String(100))
    track_id = db.Column(db.String(50))
    popularity = db.Column(db.Integer)
    time_signature = db.Column(db.Integer)
    tempo = db.Column(db.Float)
    instrumentalness = db.Column(db.Float)
    valence = db.Column(db.Float)
    energy = db.Column(db.Float)
    danceability = db.Column(db.Float)
    loudness = db.Column(db.Float)
    analysis_url = db.Column(db.String(100))


    def __repr__(self):
        return '<Song {}>'.format(self.track_name)