# app/services/spotify_services.py

import os
import spotipy.util as util
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from pprint import pprint
import requests

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_USERNAME = os.getenv('SPOTIFY_USERNAME')
SPOTIFY_REDIRECT_URL = os.getenv('SPOTIFY_REDIRECT_URL')

def spotify_api_client():
    token = spotipy.oauth2.SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
    api = spotipy.Spotify(token)
    return api

if __name__ == "__main__":
    api = spotify_api_client()    





    
    #pprint(dir(api))

     #tracks = ['4uLU6hMCjMI75M1A2tKUQC',]	2YegxR5As7BeQuVp2U6pek
