from setuptools import setup, find_packages
from os.path import dirname, join

# Get the long description from the README file
README_PATH = join(dirname(__file__), "docs/README.md")

with open(README_PATH, "r") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name = "spotifyCL",
	version = "1.3.1",
    author = "Huck Dirksmeier",
    author_email = "Huckdirks@gmail.com",
    description = "A command line interface for Spotify",
    long_description = LONG_DESCRIPTION,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Huckdirks/spotifyCL",
    packages = find_packages(),
    install_requires = ["python-dotenv", "spotipy", "rich"],
    entry_points = {
        "console_scripts": [
            "spotifycl = spotifycl.cli:select_args"
        ]
    },
    keywords = ["Spotify", "API", "Spotify API", "Web API"],
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.8",
)