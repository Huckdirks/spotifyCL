# Libraries
import spotipy
from termcolor import cprint

# Local Files
from .search import search
from .spotify_status import spotify_status

class spotify_play:
    def __init__(self, sp: spotipy.Spotify):
        self.sp: spotipy.Spotify = sp
        self.status = spotify_status(self.sp)

    def play_pause(self):
        # If the song is playing, pause it
        if self.sp.current_playback()['is_playing']:
            self.sp.pause_playback()
        else:
            self.sp.start_playback()
        return
    
    def play_track(self, NAME: str):
        RESULT = search(self.sp, NAME, 'track')
        if RESULT:
            URI = RESULT['uri']
            self.sp.start_playback(uris=[URI])
            cprint("Spotify Playing:", "green", attrs=["bold"])
            cprint("Song: " + str(RESULT["name"]), "cyan")
            cprint("Artist: " + str(RESULT["artists"][0]["name"]), "cyan")
            cprint("Album: " + str(RESULT["album"]["name"]), "cyan")
        return
    
    def play_album(self, NAME: str):
        RESULT = search(self.sp, NAME, 'album')
        if RESULT:
            URI = RESULT['uri']
            self.sp.shuffle(state=False)
            self.sp.start_playback(context_uri=URI)
            cprint("Spotify Playing:", "green", attrs=["bold"])
            cprint("Album: " + str(RESULT["name"]), "cyan")
            cprint("Artist: " + str(RESULT["artists"][0]["name"]), "cyan")
        return
    
    def play_artist(self, NAME: str):
        RESULT = search(self.sp, NAME, 'artist')
        if RESULT:
            URI = RESULT['uri']
            self.sp.start_playback(context_uri=URI)
            cprint("Spotify Playing:", "green", attrs=["bold"])
            cprint("Artist: " + str(RESULT["name"]), "cyan")
        return
    
    # Make this go through your playlists first, then if it can't find it, search everything
    def play_playlist(self, NAME: str):
        RESULT = search(self.sp, NAME, 'playlist')
        if RESULT:
            URI = RESULT['uri']
            self.sp.start_playback(context_uri=URI)
            cprint("Spotify Playing:", "green", attrs=["bold"])
            cprint("Playlist: " + str(RESULT["name"]), "cyan")
            cprint("Owner: " + str(RESULT["owner"]["display_name"]), "cyan")
        return
    
    def play_uri(self, URI: str):
        self.sp.start_playback(uris=[URI])
        cprint("Spotify Playing:", "green", attrs=["bold"])
        cprint("URI: " + str(URI), "cyan")
        return