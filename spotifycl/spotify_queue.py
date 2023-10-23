# External Libraries
import spotipy
from rich import print as rprint

# Local Files
from .search import search

class SpotifyQueue:
    """
    A class to queue songs, albums, and playlists on Spotify
    
    Attributes
    ----------
    sp : spotipy.Spotify
        The Spotify object
        
    Methods
    -------
    queue_track(NAME: str) -> None
        Queue a song
    
    queue_album(NAME: str) -> None
        Queue an album
        
    queue_playlist(NAME: str) -> None
        Queue a playlist
        
    queue_uri(URI: str) -> None
        Queue a URI
    """
    
    def __init__(self, sp: spotipy.Spotify):
        """
        Parameters
        ----------
        sp : spotipy.Spotify
            The Spotify object
        """
        
        self.sp: spotipy.Spotify = sp

    def queue_track(self, NAME: str) -> None:
        """Queue a song
        
        Will exit with an error message if there's no current Spotify session,
        or if the song is not found
        
        Parameters
        ----------
        NAME : str
            The name of the song to queue
            
        Returns
        -------
        None
        """
        
        RESULT = search(self.sp, NAME, 'track')
        if RESULT:
            try:
                URI = RESULT['uri']
                self.sp.add_to_queue(URI)
                rprint(f"[bright_green bold]Spotify Queued:[/bright_green bold]")
                rprint(f"[cyan bold]Song:[/cyan bold] [bright_green]{RESULT['name']}[/bright_green]")
                rprint(f"[cyan bold]Artist:[/cyan bold] [bright_green]{RESULT['artists'][0]['name']}[/bright_green]")
                rprint(f"[cyan bold]Album:[/cyan bold] [bright_green]{RESULT['album']['name']}[/bright_green]")
                
            except:
                #print("No Current Spotify Session!") # Spotipy already prints an error message
                exit(1)
        else:
            rprint("[red bold]No song found![/red bold]")
            exit(1)
        return
    
    def queue_album(self, NAME: str) -> None:
        """Queue an album
        
        Will exit with an error message if there's no current Spotify session,
        or if the album is not found
        
        Parameters
        ----------
        NAME : str
            The name of the album to queue
            
        Returns
        -------
        None
        """
        
        RESULT = search(self.sp, NAME, 'album')
        if RESULT:
            try:
                # Get the URI of all the tracks in the album
                TRACKS = self.sp.album_tracks(RESULT['uri'])
                TRACKS = [TRACK['uri'] for TRACK in TRACKS['items']]
                # Add all the tracks to the queue
                for TRACK in TRACKS:
                    self.sp.add_to_queue(TRACK)
                rprint(f"[bright_green bold]Spotify Queued:[/bright_green bold]")
                rprint(f"[cyan bold]Album:[/cyan bold] [bright_green]{RESULT['name']}[/bright_green]")
                rprint(f"[cyan bold]Artist:[/cyan bold] [bright_green]{RESULT['artists'][0]['name']}[/bright_green]")
                
            except:
                #print("No Current Spotify Session!") # Spotipy already prints an error message
                exit(1)
        else:
            rprint("[red bold]No album found![/red bold]")
            exit(1)
        return
    
    def queue_playlist(self, NAME: str) -> None:
        """Queue a playlist
        
        Will exit with an error message if there's no current Spotify session,
        or if the playlist is not found
        
        Parameters
        ----------
        NAME : str
            The name of the playlist to queue
            
        Returns
        -------
        None
        """
        
        RESULT = search(self.sp, NAME, 'playlist')
        if RESULT:
            try:
                # Get the URI of all the tracks in the playlist
                TRACKS = self.sp.playlist_tracks(RESULT['uri'])
                TRACKS = [TRACK['track']['uri'] for TRACK in TRACKS['items']]
                # Add all the tracks to the queue
                for TRACK in TRACKS:
                    self.sp.add_to_queue(TRACK)
                rprint(f"[bright_green bold]Spotify Queued:[/bright_green bold]")
                rprint(f"[cyan bold]Playlist:[/cyan bold] [bright_green]{RESULT['name']}[/bright_green]")
                rprint(f"[cyan bold]Owner:[/cyan bold] [bright_green]{RESULT['owner']['display_name']}[/bright_green]")
        
            except:
                #print("No Current Spotify Session!") # Spotipy already prints an error message
                exit(1)
        else:
            rprint("[red bold]No playlist found![/red bold]")
            exit(1)
        return
    
    def queue_uri(self, URI: str) -> None:
        """Queue a URI
        
        Will exit with an error message if there's no current Spotify session,
        or if the URI is not found
        
        Parameters
        ----------
        URI : str
            The URI to queue
            
        Returns
        -------
        None
        """
        
        try:
            self.sp.add_to_queue(URI)
            rprint(f"[bright_green bold]Spotify Queued:[/bright_green bold]")
            rprint(f"[cyan bold]URI:[/cyan bold] [bright_green]{URI}[/bright_green]")
        except:
            #print("No Current Spotify Session!") # Spotipy already prints an error message
            exit(1)
        return