# External Libraries
import spotipy

def search(sp: spotipy.Spotify, NAME: str, TYPE: str) -> dict | None:
    """Search Spotify for a song, album, artist, or playlist
    
    Returns
    -------
    dict
        The first result from the search
    
    None
        If no results are found
    """
    
    RESULT = sp.search(NAME, type=TYPE, limit=1)
    if RESULT[TYPE + 's']['total'] == 0:
        return None
    return RESULT[TYPE + 's']['items'][0]