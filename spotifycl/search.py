# External Libraries
import spotipy

def search(sp: spotipy.Spotify, NAME: str, TYPE: str):
    RESULT = sp.search(NAME, type=TYPE, limit=1)
    if RESULT[TYPE + 's']['total'] == 0:
        return None
    return RESULT[TYPE + 's']['items'][0]