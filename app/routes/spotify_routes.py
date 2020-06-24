#Run pip install flask-blueprint
from flask import Blueprint, jsonify, request
from app.services.spotify_services import spotify_api_client
from app.model.models import db, Songs


spotify_routes = Blueprint('spotify_routes',__name__)

@spotify_routes.route("/")
def get_track_info(tracks=['4uLU6hMCjMI75M1A2tKUQC']):
    api = spotify_api_client()
    # todo find a way to get specified track (Front-end?)
    for n_track in tracks:
        track = api.track(n_track)
        result = {'artist':track['artists'][0]['name'],'name': track['name'],
        'track_id': track['id'], 'popularity':track['popularity']}

        feat = api.audio_features(n_track)
        results2 = {'time_signature': feat[0]['time_signature'], 'tempo': feat[0]['tempo'],
        'instrumentalness': feat[0]['instrumentalness'], '': feat[0]['valence'], '': feat[0]['energy'],
        'danceability': feat[0]['danceability'], 'loudness': feat[0]['loudness'], 'key': feat[0]['key'], 'analysis_url': feat[0]['analysis_url']}

    return jsonify(result, results2)