# External Libraries
import spotipy
from termcolor import cprint

class SpotifyStatus:
    """
    A class to get the current status of Spotify
    
    Attributes
    ----------
    sp : spotipy.Spotify
        The Spotify object
        
    Methods
    -------
    status(SONG_CHANGE: bool = False)
        Get the current status of Spotify and print it
    
    convert_duration(PROGRESS: int, DURATION: int) -> str
        Convert the progress and duration from ms to minutes and seconds and return a string
    """
    
    def __init__(self, sp: spotipy.Spotify):
        """
        Parameters
        ----------
        sp : spotipy.Spotify
            The Spotify object
        """
        
        self.sp: spotipy.Spotify = sp

    def convert_duration(self, PROGRESS: int, DURATION: int) -> str:
        """Convert the progress and duration from ms to minutes and seconds,
        and return a string like so: "PROGRESS_MIN:PROGRESS_SEC / DURATION_MIN:DURATION_SEC"
        
        Example: "1:30 / 3:00"
        
        Parameters
        ----------
        PROGRESS : int
            The progress of the song in ms
        
        DURATION : int
            The duration of the song in ms
            
        Returns
        -------
        str
            The progress and duration in minutes and seconds
        """
        
        # Convert the progress and duration from ms to minutes and seconds
        PROGRESS_MIN, PROGRESS_SEC = divmod(PROGRESS, 60)
        DURATION_MIN, DURATION_SEC = divmod(DURATION, 60)

        if PROGRESS_SEC > 10 and DURATION_SEC > 10:
            return f"{PROGRESS_MIN}:{PROGRESS_SEC} / {DURATION_MIN}:{DURATION_SEC}"
        elif PROGRESS_SEC < 10 and DURATION_SEC < 10:
            return f"{PROGRESS_MIN}:0{PROGRESS_SEC} / {DURATION_MIN}:0{DURATION_SEC}"
        elif PROGRESS_SEC < 10:
            return f"{PROGRESS_MIN}:0{PROGRESS_SEC} / {DURATION_MIN}:{DURATION_SEC}"
        else:
            return f"{PROGRESS_MIN}:{PROGRESS_SEC} / {DURATION_MIN}:0{DURATION_SEC}"

        
    def status(self, SONG_CHANGE: bool = False):
        """Print the current status of Spotify
        
        Example:
            Spotify is Currently/Now Playing:
            Song: Time
            Artist: Pink Floyd
            Album: The Dark Side of the Moon
            Position: 4:20 / 6:53
            
        Will exit with an error message if there's no current song playing
        
        Parameters
        ----------
        SONG_CHANGE : bool, optional
            Whether or not the song has changed, by default False
            
        Returns
        -------
        None
        """
        
        STATUS = self.sp.current_playback()
        if STATUS is None:
            print("No song is currently playing")
            exit(1)
        
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