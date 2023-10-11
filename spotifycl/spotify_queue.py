# External Libraries
import spotipy
from termcolor import cprint

# Local Files
from .search import search

class SpotifyQueue:
    def __init__(self, sp: spotipy.Spotify):
        self.sp: spotipy.Spotify = sp

    def queue_track(self, NAME: str):
        RESULT = search(self.sp, NAME, 'track')
        if RESULT:
            URI = RESULT['uri']
            self.sp.add_to_queue(URI)
            cprint("Spotify Queued:", "green", attrs=["bold"])
            cprint("Song: " + str(RESULT["name"]), "cyan")
            cprint("Artist: " + str(RESULT["artists"][0]["name"]), "cyan")
            cprint("Album: " + str(RESULT["album"]["name"]), "cyan")
        return
    
    def queue_album(self, NAME: str):
        RESULT = search(self.sp, NAME, 'album')
        if RESULT:
            # Get the URI of all the tracks in the album
            TRACKS = self.sp.album_tracks(RESULT['uri'])
            TRACKS = [TRACK['uri'] for TRACK in TRACKS['items']]
            # Add all the tracks to the queue
            for TRACK in TRACKS:
                self.sp.add_to_queue(TRACK)
            cprint("Spotify Queued:", "green", attrs=["bold"])
            cprint("Album: " + str(RESULT["name"]), "cyan")
            cprint("Artist: " + str(RESULT["artists"][0]["name"]), "cyan")
        return
    
    def queue_playlist(self, NAME: str):
        RESULT = search(self.sp, NAME, 'playlist')
        if RESULT:
            # Get the URI of all the tracks in the playlist
            TRACKS = self.sp.playlist_tracks(RESULT['uri'])
            TRACKS = [TRACK['track']['uri'] for TRACK in TRACKS['items']]
            # Add all the tracks to the queue
            for TRACK in TRACKS:
                self.sp.add_to_queue(TRACK)
            cprint("Spotify Queued:", "green", attrs=["bold"])
            cprint("Playlist: " + str(RESULT["name"]), "cyan")
            cprint("Owner: " + str(RESULT["owner"]["display_name"]), "cyan")
        return
    
    def queue_uri(self, URI: str):
        self.sp.add_to_queue(URI)
        cprint("Spotify Queued:", "green", attrs=["bold"])
        cprint("URI: " + str(URI), "cyan")
        return