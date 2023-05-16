
class spotify_cli:
    from .set_env import set_env
    from .cli import parse_args

    def __init__(self):
        self.set_env()
        self.parse_args()


# Script entry point
def main():
    spotify_cli()