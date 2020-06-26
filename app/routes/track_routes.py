from flask import Blueprint, jsonify, request


from flask import Flask, request, jsonify
from sklearn.neighbors import NearestNeighbors
import pandas as pd
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import pandas as pd
import json
import pickle
from math import pi
import matplotlib.pyplot as plt
import io, base64

songs = pd.read_csv('app\dataset\most_popular_spotify_songs.csv')

features = ['valence', 'speechiness', 'liveness', 'instrumentalness',
             'energy', 'danceability', 'acousticness']
song_features = songs[features] 
nn = NearestNeighbors(n_neighbors=30)
nn.fit(song_features)            

app = Flask(__name__)
CORS(app)
def encoded_img(df, track_id, features):
    categories = features
    N = len(categories)
    values = df[df['track_id']==track_id][features].values.flatten().tolist()
    values += values[:1]
    values
    print(values)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    ax = plt.subplot(111, polar=True)
    plt.xticks(angles[:-1], categories, color='grey', size=8)
    ax.set_rlabel_position(0)
    plt.y_ticks([0.25,0.5,0.75,1], ["0.25", "0.5", "0.75", "1.0"], color="grey", size=7)
    plt.ylim(0,1)
    ax.plot(angles, values, linewidth=1, linestyle='solid')
    ax.fill(angles, values, 'b', alpha=0.1)
    pic_bytes = io.BytesIQ()
    plt.savefig(pic_bytes, format="png")
    pic_bytes.seek(0)
    plt.clf()
    data = base64.b64encode(pic_bytes.read()).decode("ascii")
    img = "data.image/png;base64,{}".format(data)
    return img

@app.route('/processjson', methods=['POST'])
def processjson():
    track_id = request.get_json(force=True)
    print(track_id)
    song = songs[songs["track_id"] == track_id["track_id"]].iloc[0]
    song = np.array(song[features]).reshape(1, -1)
    results = nn.kneighbors(song)
    return_dict = {}
    for index,i in enumerate(results[1][0]):
        return_dict[str(index)] = {"track_name":songs['track_name'].iloc[i], "artist":songs['artist_name'].iloc[i]}
    img = encoded_img(songs, track_id["track_id"], features)
    return jsonify({"results":return_dict, "img":img})    


