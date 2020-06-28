from flask import Flask, jsonify, request
import sqlite3
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import numpy as np
from sklearn import preprocessing  # for category encoder
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
from typing import List, Tuple
import matplotlib.pyplot as plt
import base64
import io
import pickle 
import json
from math import pi
songs = pd.read_csv("app\dataset\most_popular_spotify_songs.csv")
songs.drop_duplicates(['track_id'], inplace=True)
