# app/routes/spotify_routes.py

from flask import Blueprint, jsonify, request
from app.services.spotify_services import spotify_api_client
from app.model.models import db, Songs


spotify_routes = Blueprint('spotify_routes',__name__)


# Todo for today: add route to add new track to database
# @app.route('/add-track')
# def refresh():


#     for n_track in tracks:
#         track = api.track(n_track)
#         result = {'artist':track['artists'][0]['name'],'name': track['name'],
#         'track_id': track['id'], 'popularity':track['popularity']}

#         feat = api.audio_features(n_track)
#         addon = {'time_signature': feat[0]['time_signature'], 'tempo': feat[0]['tempo'],
#         'instrumentalness': feat[0]['instrumentalness'], 'valence': feat[0]['valence'], 'energy': feat[0]['energy'],
#         'danceability': feat[0]['danceability'], 'loudness': feat[0]['loudness'], 'key': feat[0]['key'], 'analysis_url': feat[0]['analysis_url']}

#         result.update(addon)
if __name__ == "__main__":
    pass