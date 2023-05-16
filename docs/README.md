# Spotify Command Line

## Table of Contents

- [Introduction](#introduction)
- [Installation & Setup](#installation)
  - [Installation](#installation)
  - [Setup](#setup)
- [Uses](#uses)
  - [Commands](#commands)
    - [play](#play)
    - [queue](#queue)
    - [next](#next)
    - [back](#back)
    - [status](#status)
    - [volume](#volume)
    - [shuffle & repeat](#shuffle--repeat)
- [Quality Assurance](#quality-assurance)
- [Suggestions](#suggestions)
- [Contributing](#contributing)
- [License](#license)

## Introduction

While working on my previous project: [text-excuse-generator](https://github.com/Huckdirks/text-excuse-generator), I just published my first package to [PyPi](https://pypi.org/project/text-excuse-generator/). I quickly realized that I wasn't going to be able to remember the command line arguments to pass into the required fields, and that I was bound to forget to change the version manually in the `setup.py` file every time I updated the package. So I decided to make a program that would automatically update the version number in the `setup.py` file and export a project to [PyPi](https://pypi.org/). I also added another script that would automatically create a `setup.py` file for me with the required fields.

## Installation & Setup

### Installation

To install, run the following command:

```bash
pip install spotifycl
```

You must already have Python installed on your computer.

### Setup

To setup the program, you need to have a spotify account (obviously), and you'll have to [create a new app](https://developer.spotify.com/dashboard/create) on the Spotify Developer Dashboard. Once you've created the app, find the Client ID and Client Secret in the app's settings, and then run the program in the terminal by typing `spotifycl` and follow the instructions. Once you've done that, you should be good to go!

## Uses

You can run the program by typing `spotifycl` into your terminal. You can also run the program with the `-h` or `--help` flag to get a list of all the commands and their descriptions.

Try to be as descriptive as possible when passing in the name of a playlist, album, artist, or song, because the program will find the first item that matches the name you pass in. And make sure you put quotes around any arguments that have any spaces. For example, if I try to play [Time by Pink Floyd](https://open.spotify.com/track/3TO7bbrUKrOSPGRTB5MeCz?si=99b89a567d294c81) by running [`spotifycl play time`](#play-song), it plays [Time of Our Lives by Pitbull](https://open.spotify.com/track/2bJvI42r8EF3wxjOuDav4r?si=f9995536185d4feb). While I love some Pitbull, that's not what I wanted to listen to. So if I run [`spotifycl play "time pink floyd"`](#play-song), it plays [Time by Pink Floyd](https://open.spotify.com/track/3TO7bbrUKrOSPGRTB5MeCz?si=99b89a567d294c81).

### Commands

#### play

There are 6 different ways to use the `play` command: [play](#play-1), [play song](#play-song), [play album](#play-album), [play artist](#play-artist), [play playlist](#play-playlist), and [play uri](#play-uri).

You can run any of them like so:
```bash
spotifycl play [--album/--band/--playlist/--uri] [song/album/band/playlist/uri]
```

##### play

This command will pause or play the current song depending on whether or not it's already playing.

```bash
spotifycl p
```

##### play song

This command will play the first song that matches the name of the song you pass in.

```bash
spotifycl p "song name"
```

##### play album

This command will play the first album that matches the name of the album you pass in.

```bash
spotifycl p -a "album name"
```

##### play artist

This command will play the first artist that matches the name of the artist you pass in.

```bash
spotifycl p -b "artist name"
```

##### play playlist

This command will play the first playlist that matches the name of the playlist you pass in.

```bash
spotifycl p -p "playlist name"
```

##### play uri

This command will play the song, album, artist, or playlist that matches the uri you pass in.

```bash
spotifycl p -u "uri"
```

#### queue

There are 4 different ways to use the `queue` command: [queue song](#queue-song), [queue album](#queue-album), [queue playlist](#queue-playlist), and [queue uri](#queue-uri).

You can run any of them like so:
```bash
spotifycl queue [--album/--playlist/--uri] song/[album/playlist/uri]
```

##### queue song

This command will queue the first song that matches the name of the song you pass in.

```bash
spotifycl q "song name"
```

##### queue album

This command will queue the first album that matches the name of the album you pass in.

```bash
spotifycl q -a "album name"
```

##### queue playlist

This command will queue the first playlist that matches the name of the playlist you pass in.

```bash
spotifycl q -p "playlist name"
```

##### queue uri

This command will queue the song, album, or playlist that matches the uri you pass in.

```bash
spotifycl q -u "uri"
```

#### next

This command will skip to the next song in the queue.

```bash
spotifycl next/n
```

#### back

This command will go back to the previous song in the queue.

```bash
spotifycl back/b
```

#### status

This command will print out the information about the current song.

```bash
spotifycl status/s
```

It prints out the song, artist, album, and the current time of the song.

#### volume

This command will either set the volume to the number you pass in, or it will print out the current volume.

```bash
spotifycl volume/v [number]
```

#### shuffle & repeat

These commands will either turn on or off shuffle and repeat.

```bash
spotifycl toggle/t [-s/--shuffle] [-r/--repeat]
```

## Quality Assurance

All variable, function, class, module, & file names are written in [snake_case](https://en.wikipedia.org/wiki/Snake_case) to make sure everything is consistent, and all `const` variables are written in ALL-CAPS. The variable names are quite verbose, so it should be easy enough to understand what's going on.

If there are any other/better ways to check for quality assurance, please let me know in the [suggestions](https://github.com/Huckdirks/auto-pip-exporter/discussions/new?category=suggestions)!

## Suggestions

If you have any suggestions about anything, please create a [new discussion in suggestions](https://github.com/Huckdirks/auto-pip-exporter/discussions/new?category=suggestions).

## Contributing

Contributions are always welcomed! Look at [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## License

The project is available under the [MIT](https://opensource.org/licenses/MIT) license.
