# External Libraries
import spotipy
from termcolor import cprint

class SpotifyStatus:
    def __init__(self, sp: spotipy.Spotify):
        self.sp: spotipy.Spotify = sp

    def convert_duration(self, PROGRESS: int, DURATION: int):
        # Convert the progress and duration from ms to minutes and seconds
        PROGRESS_MIN, PROGRESS_SEC: int = divmod(PROGRESS, 60)
        DURATION_MIN, DURATION_SEC: int = divmod(DURATION, 60)

        if PROGRESS_SEC > 10 and DURATION_SEC > 10:
            return f"{PROGRESS_MIN}:{PROGRESS_SEC} / {DURATION_MIN}:{DURATION_SEC}"
        elif PROGRESS_SEC < 10 and DURATION_SEC < 10:
            return f"{PROGRESS_MIN}:0{PROGRESS_SEC} / {DURATION_MIN}:0{DURATION_SEC}"
        elif PROGRESS_SEC < 10:
            return f"{PROGRESS_MIN}:0{PROGRESS_SEC} / {DURATION_MIN}:{DURATION_SEC}"
        else:
            return f"{PROGRESS_MIN}:{PROGRESS_SEC} / {DURATION_MIN}:0{DURATION_SEC}"

        
    def status(self, SONG_CHANGE: bool = False):
        STATUS = self.sp.current_playback()
        if STATUS is None:
            print("No song is currently playing")
            return
        
        if SONG_CHANGE:
            cprint("Spotify is Now Playing:", "green", attrs=["bold"])
        else:
            cprint("Spotify is Currently Playing:", "green", attrs=["bold"])

        cprint("Song: " + str(STATUS["item"]["name"]), "cyan")
        cprint("Artist: " + str(STATUS["item"]["artists"][0]["name"]), "cyan")
        cprint("Album: " + str(STATUS["item"]["album"]["name"]), "cyan")
        if not SONG_CHANGE:
            cprint("Position: " + str(self.convert_duration(int(STATUS["progress_ms"] / 1000), int(STATUS["item"]["duration_ms"] / 1000))), "cyan")
        return