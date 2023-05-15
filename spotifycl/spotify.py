
class spotify_cli:
    from set_env import set_env
    from cli import parse_args

    def __init__(self):
        self.set_env()
        self.parse_args()


if __name__ == "__main__":
    spotify_cli()