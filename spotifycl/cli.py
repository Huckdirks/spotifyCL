# Python Libraries
import argparse

# External Libraries
import spotipy
from rich import print as rprint

# Local
from .set_credentials import set_credentials
from .set_env import set_env
from .spotify_play import SpotifyPlay
from .spotify_queue import SpotifyQueue
from .spotify_status import SpotifyStatus


def set_args() -> argparse.ArgumentParser:
    """Set the arguments for the command line interface
    
    Returns
    -------
    argparse.ArgumentParser
        The argument parser
    """    
    
    parser: argparse.ArgumentParser = argparse.ArgumentParser(prog="spotify", description="Control Spotify from the command line", epilog="Made by Huck Dirksmeier")
    subparsers = parser.add_subparsers(dest="command")

    play_parser = subparsers.add_parser("play", aliases=["p"], help="Play a song, album, or playlist")
    play_parser.add_argument("song", nargs="?", help="Song name")
    play_group = play_parser.add_mutually_exclusive_group()
    play_group.add_argument("-a", "--album", help="Album name")
    play_group.add_argument("-b", "--band", help="Band name")
    play_group.add_argument("-p", "--playlist", help="Playlist name")
    play_group.add_argument("-u", "--uri", help="Spotify URI")

    queue_parser = subparsers.add_parser("queue", aliases=["q"], help="Queue a song, album, or playlist")
    queue_parser.add_argument("song", nargs="?", help="Song name")
    queue_group = queue_parser.add_mutually_exclusive_group()
    queue_group.add_argument("-a", "--album", help="Album name")
    queue_group.add_argument("-p", "--playlist", help="Playlist name")
    queue_group.add_argument("-u", "--uri", help="Spotify URI")

    subparsers.add_parser("next", aliases=["n"], help="Skip to the next song")

    subparsers.add_parser("back", aliases=["b"], help="Skip to the previous song")

    volume_parser = subparsers.add_parser("volume", aliases=["v"], help="Change the volume of the player")
    volume_parser.add_argument("level", nargs="?", type=int, help="Volume level (0-100)")

    subparsers.add_parser("status", aliases=["s"], help="Get the current status of the player")

    toggle_parser = subparsers.add_parser("toggle", aliases=["t"], help="Toggle shuffle or repeat")
    toggle_group = toggle_parser.add_mutually_exclusive_group()
    toggle_group.add_argument("-s", "--shuffle", action="store_true", help="Toggle shuffle")
    toggle_group.add_argument("-r", "--repeat", action="store_true", help="Toggle repeat")

    return parser


def select_args() -> None:
    """Select the arguments for the command line interface
    
    Will exit with an error message if there's no current Spotify session
    
    Returns
    -------
    None
    """
    
    PARSER: argparse.ArgumentParser = set_args()
    ARGS = PARSER.parse_args()
    
    set_env()
    # Spotify Client
    sp: spotipy.Spotify = set_credentials()

    if ARGS.command in ["play", "p"]:
        player: SpotifyPlay = SpotifyPlay(sp)
        if ARGS.song:
            return player.play_track(ARGS.song)
        elif ARGS.album:
            return player.play_album(ARGS.album)
        elif ARGS.band:
            return player.play_artist(ARGS.band)
        elif ARGS.playlist:
            return player.play_playlist(ARGS.playlist)
        elif ARGS.uri:
            return player.play_uri(ARGS.uri)
        else:
            return player.play_pause()


    elif ARGS.command in ["queue", "q"]:
        queuer: SpotifyQueue = SpotifyQueue(sp)
        if ARGS.song:
            return queuer.queue_track(ARGS.song)
        elif ARGS.album:
            return queuer.queue_album(ARGS.album)
        elif ARGS.playlist:
            return queuer.queue_playlist(ARGS.playlist)
        elif ARGS.uri:
            return queuer.queue_uri(ARGS.uri)
        else:
            return PARSER.print_help()

    elif ARGS.command in ["next", "n"]:
        try:
            sp.next_track()
            current_status: SpotifyStatus = SpotifyStatus(sp)
            return current_status.status(True)
        except:
            #print("No Current Spotify Session!")
            exit(1)

    elif ARGS.command in ["back", "b"]:
        try:
            sp.previous_track()
            current_status: SpotifyStatus = SpotifyStatus(sp)
            return current_status.status(True)
        except:
            #print("No Current Spotify Session!")
            exit(1)

    elif ARGS.command in ["status", "s"]:
        current_status: SpotifyStatus = SpotifyStatus(sp)
        return current_status.status()

    elif ARGS.command in ["volume", "v"]:
        if ARGS.level:
            try:
                return sp.volume(ARGS.level)
            except:
                exit(1)
        else:
            try:
                # Print the current volume
                return rprint(f"[cyan bold]Volume: {sp.current_playback()['device']['volume_percent']}[/cyan bold]")
            except:
                rprint("[red bold]No Current Spotify Session![/red bold]")
                exit(1)

    elif ARGS.command in ["toggle", "t"]:
        try:
            if ARGS.shuffle:
                if sp.current_playback()["shuffle_state"] == True:
                    sp.shuffle(False)
                    return rprint("[red bold]Shuffle is now off[/red bold]")
                else:
                    sp.shuffle(True)
                    return rprint("[green bold]Shuffle is now on[/green bold]")

            elif ARGS.repeat:
                if sp.current_playback()["repeat_state"] == "off":
                    sp.repeat("context")
                    return rprint("[green bold]Repeat is now on[/green bold]")
                elif sp.current_playback()["repeat_state"] == "context":
                    sp.repeat("track")
                    return rprint("[cyan bold]Repeat is now on (track)[/cyan bold]")
                else:
                    sp.repeat("off")
                    return rprint("[red bold]Repeat is now off[/red bold]")

            else:
                return PARSER.print_help()
        except:
            rprint("[red bold]No Current Spotify Session![/red bold]")
            exit(1)
        
    else:
        return PARSER.print_help()