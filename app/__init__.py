# __init__.py

import os
import sqlite3
from flask import Flask, jsonify
from flask import Flask
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np
from sklearn import preprocessing  # for category encoder
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
from typing import List, Tuple

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
    filePath = os.path.join(os.path.dirname(__file__), "..", "most_popular_spotify_songs.csv")
    df = pd.read_csv(filePath)
    db = df.to_sql(con=engine, index_label='id',
                   name=Songs.__tablename__, if_exists='replace')

    '''    
        This pre_process function takes in a pandas dataframe and runs it through 
        encoding code to standardize certain features, it also onehotencodes the dataframe to
        make it all numeric.
    '''
    def pre_process(df):
        time_sig_encoding = {'0/4': 0, '1/4': 1,
                                '3/4': 3, '4/4': 4,
                                '5/4': 5}
        key_encoding = {'A': 0, 'A#': 1, 'B': 2,
                        'C': 3,  'C#': 4,  'D': 5,
                        'D#': 6, 'E': 7, 'F': 8,
                        'F#': 9, 'G': 10, 'G#': 11}
        mode_encoding = {'Major': 0, 'Minor': 1}
        df['key'] = df['key'].map(key_encoding)
        df['time_signature'] = df['time_signature'].map(time_sig_encoding)
        df['mode'] = df['mode'].map(mode_encoding)
        # helper function to one hot encode genre

        def encode_and_bind(original_dataframe, feature_to_encode):
            dummies = pd.get_dummies(original_dataframe[[feature_to_encode]])
            res = pd.concat([original_dataframe, dummies], axis=1)
            return(res)
        df = encode_and_bind(df, 'genre')
        return df

    '''
        This will run the nearest neighbors model when we instantiate the app.
    '''
    conn = sqlite3.connect('spot_wavez.db')
    database = pd.read_sql_query("SELECT * FROM Songs", conn)
    processed_df = pre_process(database)

    neigh = NearestNeighbors(n_neighbors=11)
    features = list(processed_df.columns[5:])
    X = processed_df[features].values
    neigh.fit(X)

    '''
        Takes in a dataframe, a feature set array and a song ID and 
        returns a list of tuples of Artist Name and Track Name
    '''
    def closest_ten(df: pd.DataFrame, X_array: np.ndarray, song_id: int) -> List[Tuple]:
        song = df.iloc[song_id]
        X_song = X[song_id]
        _, neighbors = neigh.kneighbors(np.array([X_song]))
        return neighbors[0][1:]

    # accepts the cursor and the row as a tuple and returns a dictionary result and you can object column by name 
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

     #@app.route('/track/<track_id>', methods=['GET'])
     #def track(track_id):
         #track_id = int(track_id)
         #conn = sqlite3.connect('spot_wavez.db')
         #conn.row_factory = dict_factory
         #curs = conn.cursor()
         #songlist = []
         #song_recs = closest_ten(database, X, track_id)
         #for idx in song_recs:
             #song = curs.execute(
                 #f'SELECT DISTINCT * FROM Songs WHERE id=={idx};').fetchone()
             #songlist.append(song)
         #return jsonify(songlist)

    
    app.register_blueprint(spotify_routes)

    return app

if __name__ == "__main__":
    app = create_app() # invokes the create_app function
    app.run(debug=True) # then runs the app
    #tracks = ['4uLU6hMCjMI75M1A2tKUQC',]