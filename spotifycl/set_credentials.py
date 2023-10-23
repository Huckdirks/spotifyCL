# Python Libraries
from os.path import dirname, isfile

# External Libraries
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from rich import print as rprint


def set_credentials() -> spotipy.Spotify:
    """Set the credentials for the Spotify API
    
    Returns
    -------
    spotipy.Spotify
        The Spotify API object
    """
    
    PROJECT_DIR: str = dirname(__file__)
    
    ENV_PATH: str = f"{PROJECT_DIR}/.env"
    if not isfile(ENV_PATH):
        rprint("[red bold].env file not found![/red bold]")
        exit(1)
    
    load_dotenv(ENV_PATH)
    SCOPE: str = "user-read-playback-state,user-modify-playback-state"
    CACHE_PATH: str = f"{PROJECT_DIR}/.cache"
    
    cache_handle: spotipy.CacheFileHandler = spotipy.CacheFileHandler(cache_path = CACHE_PATH)
    credentials_manager: spotipy.SpotifyOAuth = SpotifyOAuth(scope = SCOPE, cache_handler = cache_handle)
    sp: spotipy.Spotify = spotipy.Spotify(client_credentials_manager = credentials_manager)
    return sp