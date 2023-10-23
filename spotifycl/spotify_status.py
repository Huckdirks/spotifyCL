# External Libraries
import spotipy
from rich import print as rprint

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
    """
    
    def __init__(self, sp: spotipy.Spotify):
        """
        Parameters
        ----------
        sp : spotipy.Spotify
            The Spotify object
        """
        
        self.sp: spotipy.Spotify = sp

    def __convert_duration(self, PROGRESS: int, DURATION: int) -> str:
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
            rprint("[red bold]No song is currently playing![/red bold]")
            exit(1)
        
        if SONG_CHANGE:
            rprint("[bright_green bold]Spotify is Now Playing:[/bright_green bold]")
        else:
            rprint("[bright_green bold]Spotify is Currently Playing:[/bright_green bold]")

        rprint(f"[cyan bold]Song:[/cyan bold] [bright_green]{STATUS['item']['name']}[/bright_green]")
        rprint(f"[cyan bold]Artist:[/cyan bold] [bright_green]{STATUS['item']['artists'][0]['name']}[/bright_green]")
        rprint(f"[cyan bold]Album:[/cyan bold] [bright_green]{STATUS['item']['album']['name']}[/bright_green]")
        
        if not SONG_CHANGE:
            rprint(f"[cyan bold]Position:[/cyan bold] [bright_green]{self.__convert_duration(int(STATUS['progress_ms'] / 1000), int(STATUS['item']['duration_ms'] / 1000))}[/bright_green]")
        return