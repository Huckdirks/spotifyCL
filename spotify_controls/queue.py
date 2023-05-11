import spotipy
from .search import search

class spotify_queue:
    def __init__(self, sp: spotipy.Spotify):
        self.sp: spotipy.Spotify = sp

    def queue_track(self, NAME: str):
        URI = search(self.sp, NAME, 'track')
        if URI:
            self.sp.add_to_queue(URI)
        return
    
    def queue_album(self, NAME: str):
        URI = search(self.sp, NAME, 'album')
        if URI:
            self.sp.add_to_queue(URI)
        return
    
    def queue_playlist(self, NAME: str):
        URI = search(self.sp, NAME, 'playlist')
        if URI:
            self.sp.add_to_queue(URI)
        return
    
    def queue_uri(self, URI: str):
        return self.sp.add_to_queue(URI)