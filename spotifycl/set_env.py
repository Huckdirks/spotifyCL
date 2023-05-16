from os.path import dirname, join, isfile


def set_env(self):
    ENV_PATH = join(dirname(__file__), '.env')
    if isfile(ENV_PATH):
        return
    
    print(".env file not found")
    print("To use this program, you need to set up a Spotify Developer Account & App here:")
    print("https://developer.spotify.com/dashboard/create")
    print("Then, get the following information from the app's settings page and input it below:")
    SPOTIPY_CLIENT_ID = input("Enter your Spotify Client ID: ")
    SPOTIPY_CLIENT_SECRET = input("Enter your Spotify Client Secret: ")
    SPOTIPY_REDIRECT_URI = input("Enter your Spotify Redirect URI: ")

    ENV_TEXT = ["# Spotify",
                f"SPOTIPY_CLIENT_ID=\"{SPOTIPY_CLIENT_ID}\"",
                f"SPOTIPY_CLIENT_SECRET=\"{SPOTIPY_CLIENT_SECRET}\"",
                f"SPOTIPY_REDIRECT_URI=\"{SPOTIPY_REDIRECT_URI}\""
            ]
    
    with open(ENV_PATH, 'w') as dotenv:
        dotenv.writelines('\n'.join(ENV_TEXT))

    print("Environment variables set successfully")
    return