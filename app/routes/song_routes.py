from flask import Flask, request, jsonify
from sklearn.neighbors import NearestNeighbors
import pandas as pd


df = pd.read_csv("app\dataset\most_popular_spotify_songs.csv")
def process_input(song_id, return_json=True):
    c = ["duration_ms", "genre", "artist_name", "track_id", "track_name", "key", "mode"] #columns to omit
    song = df[df["track_id"] == song_id].iloc[0] #get song
    df_selected = df.copy()
    if not pd.isnull(song["genre"]):
        df_selected = df[df["genre"] == song["genre"]]
    nn = NearestNeighbors(n_neighbors=31, algorithm="kd_tree")
    nn.fit(df_selected.drop(columns=c))
    song = song.drop(index=c)
    song = np.array(song).reshape(1, -1)
    if return_json is False:
        return df_selected.iloc[nn.kneighbors(song)[1][0][1:]]
    return df_selected.iloc[nn.kneighbors(song)[1][0][1:]].to_json(orient="records")


app = Flask(__name__) 

@app.route('/song/<song_id>', methods=['GET'])
def song(song_id):
    """Route for recommendations based on song selected"""
    return process_input(song_id)   
         

         
