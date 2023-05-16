from os.path import dirname, join, isfile
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv


def set_credentials():
    ENV_PATH = join(dirname(__file__), '.env')
    if not isfile(ENV_PATH):
        print(".env file not found")
        exit()
    
    load_dotenv(ENV_PATH)
    scope = "user-read-playback-state user-modify-playback-state"
    sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))
    return sp