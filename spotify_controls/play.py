import spotipy
from .set_credentials import set_credentials
from .search import search

class spotify_play:
    def __init__(self):
        self.sp: spotipy.Spotify = set_credentials()

    def play_pause(self):
        # If the song is playing, pause it
        if self.sp.current_playback()['is_playing']:
            self.sp.pause_playback()
        else:
            self.sp.start_playback()
        return
    
    def play_track(self, NAME: str):
        URI = search(self.sp, NAME, 'track')
        if URI:
            self.sp.start_playback(uris=[URI])
        return
    
    def play_album(self, NAME: str):
        URI = search(self.sp, NAME, 'album')
        if URI:
            self.sp.shuffle(state=False)
            self.sp.start_playback(context_uri=URI)
        return
    
    def play_artist(self, NAME: str):
        URI = search(self.sp, NAME, 'artist')
        if URI:
            self.sp.start_playback(context_uri=URI)
        return
    
    # Make this go through your playlists first, then if it can't find it, search everything
    def play_playlist(self, NAME: str):
        URI = search(self.sp, NAME, 'playlist')
        if URI:
            self.sp.start_playback(context_uri=URI)
        return
    
    def play_uri(self, URI: str):
        return self.sp.start_playback(context_uri=URI)