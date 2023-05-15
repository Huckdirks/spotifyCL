
class spotify_cli:
    from _set_env import set_env
    from _cli import parse_args

    def __init__(self):
        self.set_env()
        self.parse_args()


if __name__ == "__main__":
    spotify_cli()