# app/__init__.py

from flask import Flask

from app.routes.spotify_routes import spotify_routes

def create_app():
    # initializes the app
    app = Flask(__name__)
    #Import the blueprint first and install Blueprint
    app.register_blueprint(spotify_routes)
    return app

if __name__ == "__main__":
    app = create_app() # invokes the create_app function
    app.run(debug=True) # then runs the app