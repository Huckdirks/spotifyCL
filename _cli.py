import argparse

def parse_args(self):
    parser = argparse.ArgumentParser(prog="spotify", description="Control Spotify from the command line", epilog="Made by Huck Dirksmeier")
    subparsers = parser.add_subparsers(dest="command")

    play_parser = subparsers.add_parser("play", aliases=["p"], help="Play a song, album, or playlist")
    play_parser.add_argument("song", nargs="?", help="Song name")
    play_group = play_parser.add_mutually_exclusive_group()
    play_group.add_argument("-a", "--album", help="Album name")
    play_group.add_argument("-b", "--band", help="Band name")
    play_group.add_argument("-l", "--list", help="Playlist name")
    play_group.add_argument("-u", "--uri", help="Spotify URI")

    queue_parser = subparsers.add_parser("queue", aliases=["q"], help="Queue a song, album, or playlist")
    queue_parser.add_argument("song", nargs="?", help="Song name")
    queue_group = queue_parser.add_mutually_exclusive_group()
    queue_group.add_argument("-a", "--album", help="Album name")
    queue_group.add_argument("-l", "--list", help="Playlist name")
    queue_group.add_argument("-u", "--uri", help="Spotify URI")

    next_parser = subparsers.add_parser("next", aliases=["n"], help="Skip to the next song")

    back_parser = subparsers.add_parser("back", aliases=["b"], help="Skip to the previous song")

    volume_parser = subparsers.add_parser("volume", aliases=["v"], help="Change the volume of the player")
    volume_group = volume_parser.add_mutually_exclusive_group()
    volume_group.add_argument("level", nargs="?", type=int, help="Volume level (0-100)")
    volume_group.add_argument("-u", "--up", action="store_true", help="Increase volume by 10")
    volume_group.add_argument("-d", "--down", action="store_true", help="Decrease volume by 10")

    status_parser = subparsers.add_parser("status", aliases=["s"], help="Get the current status of the player")

    toggle_parser = subparsers.add_parser("toggle", aliases=["t"], help="Toggle shuffle or repeat")
    toggle_group = toggle_parser.add_mutually_exclusive_group()
    toggle_group.add_argument("-s", "--shuffle", action="store_true", help="Toggle shuffle")
    toggle_group.add_argument("-r", "--repeat", action="store_true", help="Toggle repeat")

    return arg_selector(parser)


def arg_selector(parser):
    args = parser.parse_args()

    #if args.command == "play" or args.command == "p":
    if args.command in ["play", "p"]:
        if args.album:
            print(args.album)
        elif args.band:
            print(args.band)
        elif args.list:
            print(args.list)
        elif args.uri:
            print(args.uri)
        else:
            print(args.song)

    elif args.command in ["queue", "q"]:
        if args.album:
            print(args.album)
        elif args.list:
            print(args.list)
        elif args.uri:
            print(args.uri)
        else:
            print(args.song)

    elif args.command in ["next", "n"]:
        # Code for next command
        pass

    elif args.command in ["back", "b"]:
        # Code for back command
        pass

    elif args.command in ["status", "s"]:
        # Code for status command
        pass

    elif args.command in ["volume", "v"]:
        if args.level:
            print(args.level)
        elif args.up:
            print(args.up)
        elif args.down:
            print(args.down)
        else:
            # Get current volume
            pass

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



if __name__ == "__main__":
    parse_args()