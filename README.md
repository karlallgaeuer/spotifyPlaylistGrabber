# Grab the tracklist from a Spotify playlist
## Installation
1. Download and install Git
2. Clone project from Git (https://github.com/karlallgaeuer/spotifyPlaylistGrabber)
3. Have python installed (3.7.9)
4. Run ```pip install spotipy``` in the command line (this library is required) (2.17.1)

## How to use the App
1. Before using the app you have to get a Spotify Client ID and a Client Secret Key from the Spotify website (https://developer.spotify.com/dashboard/login). 
2. Next copy-paste those two keys into the "config.txt"-File.
3. To start the app open the "start.bat"-File or run ```python playlistgrabberSpotify.py``` after switching to the correct directory with ```cd [directory]``` in the command line (Windows).

Running the app will create a new file called "tracklist.txt". If you get the tracklist of another playlist it will be overwritten.
