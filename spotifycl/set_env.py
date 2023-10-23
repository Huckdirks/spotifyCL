# Python Libraries
from os.path import dirname, join, isfile

# External Libraries
from rich import print as rprint
from rich.prompt import Prompt

def set_env():
    """Set the environment variables for the Spotify API
    
    Will create a .env file if one does not exist, and will prompt the user for the necessary information
    
    Returns
    -------
    None
    """
    
    ENV_PATH = join(dirname(__file__), '.env')
    if isfile(ENV_PATH):
        return
    
    """ cprint("To use this program, you need to set up a Spotify Developer Account & App here:", "red")
    cprint("https://developer.spotify.com/dashboard/create", "red", attrs=["underline"])
    cprint("Then, get the following information from the app's settings page and input it below:\n", "red") """
    rprint("[red]To use this program, you need to set up a Spotify Developer Account & App here:[/red]")
    rprint("[red underline]https://developer.spotify.com/dashboard/create[/red underline]")
    rprint("[red]Then, get the following information from the app's settings page and input it below:\n[/red]")

    """ SPOTIPY_CLIENT_ID = input("Enter your Spotify Client ID: ")
    SPOTIPY_CLIENT_SECRET = input("Enter your Spotify Client Secret: ")
    SPOTIPY_REDIRECT_URI = input("Enter your Spotify Redirect URI: ") """
    SPOTIPY_CLIENT_ID = Prompt.ask("[green bold]Enter your Spotify Client ID[/green bold]")
    SPOTIPY_CLIENT_SECRET = Prompt.ask("[green bold]Enter your Spotify Client Secret[/green bold]")
    SPOTIPY_REDIRECT_URI = Prompt.ask("[green bold]Enter your Spotify Redirect URI[/green bold]")

    ENV_TEXT = ["# Spotify",
                f"SPOTIPY_CLIENT_ID=\"{SPOTIPY_CLIENT_ID}\"",
                f"SPOTIPY_CLIENT_SECRET=\"{SPOTIPY_CLIENT_SECRET}\"",
                f"SPOTIPY_REDIRECT_URI=\"{SPOTIPY_REDIRECT_URI}\""
            ]
    
    try:
        with open(ENV_PATH, 'w') as dotenv:
            dotenv.writelines('\n'.join(ENV_TEXT))
    except Exception as e:
        rprint(f"[red bold]Failed to write to .env file: {e}[/red bold]")
        exit(1)

    #print("Environment variables set successfully")
    rprint("\n[green bold]Environment variables set successfully![/green bold]\n")
    return