# Libraries
import argparse
import spotipy
from pprint import pprint

# Local
from spotify_controls import set_credentials
from spotify_controls import play
from spotify_controls import queue
from spotify_controls import status


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

    return _arg_selector(parser)


def _arg_selector(parser):
    args = parser.parse_args()
    # Spotify Client
    sp: spotipy.Spotify = set_credentials.set_credentials()

    if args.command in ["play", "p"]:
        player = play.spotify_play(sp)
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
        queuer = queue.spotify_queue(sp)
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
        current_status = status.spotify_status(sp)
        current_status.status(True)

    elif args.command in ["back", "b"]:
        sp.previous_track()
        current_status = status.spotify_status(sp)
        current_status.status(True)

    elif args.command in ["status", "s"]:
        current_status = status.spotify_status(sp)
        current_status.status()

    elif args.command in ["volume", "v"]:
        if args.level:
            sp.volume(args.level)
        else:
            return parser.print_help()

    elif args.command in ["toggle", "t"]:
        if args.shuffle:
            print(args.shuffle)
        elif args.repeat:
            print(args.repeat)
        else:
            # Help message
            return parser.print_help()
    else:
        # Help message
        return parser.print_help()