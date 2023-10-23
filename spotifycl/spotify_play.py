# External Libraries
import spotipy
from rich import print as rprint

# Local Files
from .search import search

class SpotifyPlay:
    """
    A class to play songs, albums, artists, and playlists on Spotify
    
    Attributes
    ----------
    sp : spotipy.Spotify
        The Spotify object
        
    Methods
    -------
    play_pause() -> None
        Play or pause the current song
    
    play_track(NAME: str) -> None
        Play a song
    
    play_album(NAME: str) -> None
        Play an album
    
    play_artist(NAME: str) -> None
        Play an artist
        
    play_playlist(NAME: str) -> None
        Play a playlist
        
    play_uri(URI: str) -> None
        Play a URI
    """
    
    def __init__(self, sp: spotipy.Spotify):
        """
        Parameters
        ----------
        sp : spotipy.Spotify
            The Spotify object
        """
        
        self.sp: spotipy.Spotify = sp

    def play_pause(self) -> None:
        """Play or pause the current song
        
        Will exit with an error message if there's no current Spotify session
        
        Returns
        -------
        None
        """
        
        try:
            if self.sp.current_playback()['is_playing']:
                self.sp.pause_playback()
            else:
                self.sp.start_playback()
        except:
            rprint("[red bold]No Current Spotify Session![/red bold]")
            exit(1)
        return
    
    def play_track(self, NAME: str) -> None:
        """Play a song 
        
        Will exit with an error message if there's no current Spotify session,
        or if the song is not found
        
        Parameters
        ----------
        NAME : str
            The name of the song to play
        
        Returns
        -------
        None
        """
        
        RESULT = search(self.sp, NAME, 'track')
        if RESULT:
            try:
                URI = RESULT['uri']
                self.sp.start_playback(uris=[URI])
                rprint(f"[bright_green bold]Spotify Playing:[/bright_green bold]")
                rprint(f"[cyan bold]Song:[/cyan bold] [bright_green]{RESULT['name']}[/bright_green]")
                rprint(f"[cyan bold]Artist:[/cyan bold] [bright_green]{RESULT['artists'][0]['name']}[/bright_green]")
                rprint(f"[cyan bold]Album:[/cyan bold] [bright_green]{RESULT['album']['name']}[/bright_green]")
                
            except:
                #print("No Current Spotify Session!") # Spotipy already sends an error message
                exit(1)
        else:
            rprint("[red bold]No song found![/red bold]")
            exit(1)
        return
    
    def play_album(self, NAME: str) -> None:
        """Play an album
        
        Will exit with an error message if there's no current Spotify session,
        or if the album is not found
        
        Parameters
        ----------
        NAME : str
            The name of the album to play
            
        Returns
        -------
        None
        """
        
        RESULT = search(self.sp, NAME, 'album')
        if RESULT:
            try:
                URI = RESULT['uri']
                self.sp.shuffle(state=False)
                self.sp.start_playback(context_uri=URI)
                rprint(f"[bright_green bold]Spotify Playing:[/bright_green bold]")
                rprint(f"[cyan bold]Album:[/cyan bold] [bright_green]{RESULT['name']}[/bright_green]")
                rprint(f"[cyan bold]Artist:[/cyan bold] [bright_green]{RESULT['artists'][0]['name']}[/bright_green]")

            except:
                #print("No Current Spotify Session!") # Spotipy already sends an error message
                exit(1)
        else:
            rprint("[red bold]No album found![/red bold]")
            exit(1)
        return
    
    def play_artist(self, NAME: str) -> None:
        """Play an artist's music
        
        Will exit with an error message if there's no current Spotify session,
        or if the artist is not found
        
        Parameters
        ----------
        NAME : str
            The name of the artist to play
            
        Returns
        -------
        None
        """
        
        RESULT = search(self.sp, NAME, 'artist')
        if RESULT:
            try:
                URI = RESULT['uri']
                self.sp.start_playback(context_uri=URI)
                rprint(f"[bright_green bold]Spotify Playing:[/bright_green bold]")
                rprint(f"[cyan bold]Artist:[/cyan bold] [bright_green]{RESULT['name']}[/bright_green]")
            except:
                #print("No Current Spotify Session!") # Spotipy already sends an error message
                exit(1)
        else:
            rprint("[red bold]No artist found![/red bold]")
            exit(1)
        return
    
    # TODO: Make this go through your playlists first, then if it can't find it, search everything
    def play_playlist(self, NAME: str) -> None:
        """Play a playlist
        
        Will exit with an error message if there's no current Spotify session,
        or if the playlist is not found
        
        Parameters
        ----------
        NAME : str
            The name of the playlist to play
            
        Returns
        -------
        None
        """
        
        RESULT = search(self.sp, NAME, 'playlist')
        if RESULT:
            try:
                URI = RESULT['uri']
                self.sp.start_playback(context_uri=URI)
                rprint(f"[bright_green bold]Spotify Playing:[/bright_green bold]")
                rprint(f"[cyan bold]Playlist:[/cyan bold] [bright_green]{RESULT['name']}[/bright_green]")
                rprint(f"[cyan bold]Owner:[/cyan bold] [bright_green]{RESULT['owner']['display_name']}[/bright_green]")
            except:
                #print("No Current Spotify Session!") # Spotipy already sends an error message
                exit(1)
        else:
            rprint("[red bold]No playlist found![/red bold]")
            exit(1)
        return
    
    def play_uri(self, URI: str) -> None:
        """Play a URI
        
        Will exit with an error message if there's no current Spotify session,
        or if the URI is invalid
        
        Parameters
        ----------
        URI : str
            The URI to play
            
        Returns
        -------
        None
        """
        
        try:
            self.sp.start_playback(uris=[URI])
            rprint(f"[bright_green bold]Spotify Playing:[/bright_green bold]")
            rprint(f"[cyan bold]URI:[/cyan bold] [bright_green]{URI}[/bright_green]")
        except:
            #print("No Current Spotify Session!") # Spotipy already sends an error message
            exit(1)
        return