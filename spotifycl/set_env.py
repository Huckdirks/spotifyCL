from os.path import dirname, join, isfile


def set_env(self):
    ENV_PATH = join(dirname(dirname(__file__)), '.env')
    #ENV_PATH = join(dirname(__file__), '.env')
    if isfile(ENV_PATH):
        return
    
    print(".env file not found")
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
