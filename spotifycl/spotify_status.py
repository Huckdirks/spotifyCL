from termcolor import cprint

class spotify_status:
    #def __init__(self, sp: spotipy.Spotify):
    def __init__(self, sp):
        #self.sp: spotipy.Spotify = sp
        self.sp = sp

    def convert_duration(self, progress: int, duration: int):
        # Convert the progress and duration from ms to minutes and seconds
        progress_min, progress_sec = divmod(progress, 60)
        duration_min, duration_sec = divmod(duration, 60)

        if progress_sec > 10 and duration_sec > 10:
            return f"{progress_min}:{progress_sec} / {duration_min}:{duration_sec}"
        elif progress_sec < 10 and duration_sec < 10:
            return f"{progress_min}:0{progress_sec} / {duration_min}:0{duration_sec}"
        elif progress_sec < 10:
            return f"{progress_min}:0{progress_sec} / {duration_min}:{duration_sec}"
        else:
            return f"{progress_min}:{progress_sec} / {duration_min}:0{duration_sec}"

        

    #def status(self, SONG_CHANGE: bool = False):
    def status(self, SONG_CHANGE: bool = False):
        status = self.sp.current_playback()
        if status is None:
            print("No song is currently playing")
            return
        
        if SONG_CHANGE:
            cprint("Spotify is Now Playing:", "green", attrs=["bold"])
        else:
            cprint("Spotify is Currently Playing:", "green", attrs=["bold"])

        cprint("Song: " + str(status["item"]["name"]), "cyan")
        cprint("Artist: " + str(status["item"]["artists"][0]["name"]), "cyan")
        cprint("Album: " + str(status["item"]["album"]["name"]), "cyan")
        if not SONG_CHANGE:
            cprint("Position: " + str(self.convert_duration(int(status["progress_ms"] / 1000), int(status["item"]["duration_ms"] / 1000))), "cyan")
        return