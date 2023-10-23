# External Libraries
import spotipy

def search(sp: spotipy.Spotify, NAME: str, TYPE: str) -> dict | None:
    """Search Spotify for a song, album, artist, or playlist
    
    Parameters
    ----------
    sp : spotipy.Spotify
        The Spotify object
    
    NAME : str
        The name of the song, album, artist, or playlist to search for
        
    TYPE : str
        The type of search to perform (track, album, artist, or playlist)
        
    
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