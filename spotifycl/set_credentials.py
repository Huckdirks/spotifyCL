# Python Libraries
from os.path import dirname, join, isfile

# External Libraries
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv


def set_credentials() -> spotipy.Spotify:
    ENV_PATH: str = join(dirname(__file__), '.env')
    if not isfile(ENV_PATH):
        print(".env file not found")
        exit()
    
    load_dotenv(ENV_PATH)
    SCOPE = "user-read-playback-state user-modify-playback-state"
    sp: spotipy.Spotify = spotipy.Spotify(client_credentials_manager = SpotifyOAuth(scope = SCOPE))
    return sp