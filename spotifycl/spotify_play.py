# External Libraries
import spotipy
from termcolor import cprint

# Local Files
from .search import search

class SpotifyPlay:
    def __init__(self, sp: spotipy.Spotify):
        self.sp: spotipy.Spotify = sp

    def play_pause(self):
        # If the song is playing, pause it
        """ if self.sp.current_playback()['is_playing']:
            self.sp.pause_playback()
        else:
            self.sp.start_playback()
        return """
        try:
            if self.sp.current_playback()['is_playing']:
                self.sp.pause_playback()
            else:
                self.sp.start_playback()
        except:
            print("No Current Spotify Session!")
            exit(1)
    
    def play_track(self, NAME: str):
        RESULT = search(self.sp, NAME, 'track')
        if RESULT:
            try:
                URI = RESULT['uri']
                self.sp.start_playback(uris=[URI])
                cprint("Spotify Playing:", "green", attrs=["bold"])
                cprint("Song: " + str(RESULT["name"]), "cyan")
                cprint("Artist: " + str(RESULT["artists"][0]["name"]), "cyan")
                cprint("Album: " + str(RESULT["album"]["name"]), "cyan")
            except:
                #print("No Current Spotify Session!") # Spotipy already sends an error message
                exit(1)
        else:
            print("No song found")
            exit(1)
        return
    
    def play_album(self, NAME: str):
        RESULT = search(self.sp, NAME, 'album')
        if RESULT:
            try:
                URI = RESULT['uri']
                self.sp.shuffle(state=False)
                self.sp.start_playback(context_uri=URI)
                cprint("Spotify Playing:", "green", attrs=["bold"])
                cprint("Album: " + str(RESULT["name"]), "cyan")
                cprint("Artist: " + str(RESULT["artists"][0]["name"]), "cyan")
            except:
                #print("No Current Spotify Session!") # Spotipy already sends an error message
                exit(1)
        else:
            print("No album found")
            exit(1)
        return
    
    def play_artist(self, NAME: str):
        RESULT = search(self.sp, NAME, 'artist')
        if RESULT:
            try:
                URI = RESULT['uri']
                self.sp.start_playback(context_uri=URI)
                cprint("Spotify Playing:", "green", attrs=["bold"])
                cprint("Artist: " + str(RESULT["name"]), "cyan")
            except:
                #print("No Current Spotify Session!") # Spotipy already sends an error message
                exit(1)
        else:
            print("No artist found")
            exit(1)
        return
    
    # Make this go through your playlists first, then if it can't find it, search everything
    def play_playlist(self, NAME: str):
        RESULT = search(self.sp, NAME, 'playlist')
        if RESULT:
            try:
                URI = RESULT['uri']
                self.sp.start_playback(context_uri=URI)
                cprint("Spotify Playing:", "green", attrs=["bold"])
                cprint("Playlist: " + str(RESULT["name"]), "cyan")
                cprint("Owner: " + str(RESULT["owner"]["display_name"]), "cyan")
            except:
                #print("No Current Spotify Session!") # Spotipy already sends an error message
                exit(1)
        else:
            print("No playlist found")
            exit(1)
        return
    
    def play_uri(self, URI: str):
        try:
            self.sp.start_playback(uris=[URI])
            cprint("Spotify Playing:", "green", attrs=["bold"])
            cprint("URI: " + str(URI), "cyan")
        except:
            #print("No Current Spotify Session!") # Spotipy already sends an error message
            exit(1)
        return