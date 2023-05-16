# Libraries
import argparse
import spotipy
from termcolor import cprint

# Local
# Will break if you try to run by calling python/3 because of the . but it makes it work as a package
from .set_credentials import set_credentials
from .spotify_play import spotify_play
from .spotify_queue import spotify_queue
from .spotify_status import spotify_status


def parse_args(self):
    parser = argparse.ArgumentParser(prog="spotify", description="Control Spotify from the command line", epilog="Made by Huck Dirksmeier")
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

    return arg_selector(parser)


def arg_selector(parser):
    args = parser.parse_args()
    # Spotify Client
    sp: spotipy.Spotify = set_credentials()

    if args.command in ["play", "p"]:
        player = spotify_play(sp)
        if args.song:
            player.play_track(args.song)
        elif args.album:
            player.play_album(args.album)
        elif args.band:
            player.play_artist(args.band)
        elif args.playlist:
            player.play_playlist(args.playlist)
        elif args.uri:
            player.play_uri(args.uri)
        else:
            player.play_pause()


    elif args.command in ["queue", "q"]:
        queuer = spotify_queue(sp)
        if args.song:
            queuer.queue_track(args.song)
        elif args.album:
            queuer.queue_album(args.album)
        elif args.playlist:
            queuer.queue_playlist(args.playlist)
        elif args.uri:
            queuer.queue_uri(args.uri)
        else:
            return parser.print_help()

    elif args.command in ["next", "n"]:
        sp.next_track()
        current_status = spotify_status(sp)
        current_status.status(True)

    elif args.command in ["back", "b"]:
        sp.previous_track()
        current_status = spotify_status(sp)
        current_status.status(True)

    elif args.command in ["status", "s"]:
        current_status = spotify_status(sp)
        current_status.status()

    elif args.command in ["volume", "v"]:
        if args.level:
            sp.volume(args.level)
        else:
            # Print the current volume
            cprint(f"Volume: {sp.current_playback()['device']['volume_percent']}", "cyan", attrs=["bold"])

    elif args.command in ["toggle", "t"]:
        if args.shuffle:
            if sp.current_playback()["shuffle_state"] == True:
                sp.shuffle(False)
                cprint("Shuffle is now off", "red", attrs=["bold"])
            else:
                sp.shuffle(True)
                cprint("Shuffle is now on", "green", attrs=["bold"])

        elif args.repeat:
            if sp.current_playback()["repeat_state"] == "off":
                sp.repeat("context")
                cprint("Repeat is now on", "green", attrs=["bold"])
            elif sp.current_playback()["repeat_state"] == "context":
                sp.repeat("track")
                cprint("Repeat is now on (track)", "cyan", attrs=["bold"])
            else:
                sp.repeat("off")
                cprint("Repeat is now off", "red", attrs=["bold"])

        else:
            return parser.print_help()
        
    else:
        return parser.print_help()