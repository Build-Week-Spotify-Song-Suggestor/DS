# app/__init__.py

import os
from flask import Flask
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

import pandas as pd

from app.routes.spotify_routes import spotify_routes
from app.model.models import Songs


DATABASE_URI = "sqlite:///spot_wavez.db"

def create_app():
    # initializes the app
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    
    # allows you to define tables and models in one go
    # populating it with the data in the csv file
    engine = create_engine(DATABASE_URI)
    Songs.metadata.create_all(engine)
    filePath = os.path.join(os.path.dirname(__file__), "dataset", "most_popular_spotify_songs.csv")
    df = pd.read_csv(filePath)
    db = df.to_sql(con=engine, index_label='id',
                   name=Songs.__tablename__, if_exists='replace')

    app.register_blueprint(spotify_routes)

    return app

if __name__ == "__main__":
    app = create_app() # invokes the create_app function
    app.run(debug=True) # then runs the app