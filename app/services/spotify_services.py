# app/services/spotify_services.py


import os
import spotipy.util as stil
import spotipy
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_USERNAME = os.getenv('SPOTIFY_USERNAME')
SPOTIFY_REDIRECT_URL = os.getenv('SPOTIFY_REDIRECT_URL')

def spotify_api_client():
    try:
        token = stil.prompt_for_user_token(
            SPOTIFY_USERNAME, client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URL)
    except:
        os.remove(f".cache-{SPOTIFY_USERNAME}")
        token = stil.prompt_for_user_token(
            SPOTIFY_USERNAME, client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URL)
    api = spotipy.Spotify(auth=token)
    return api

if __name__ == "__main__":
    api = spotify_api_client()
    #pprint(dir(api))

    tracks = ['4uLU6hMCjMI75M1A2tKUQC',]
