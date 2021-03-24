# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 23:39:20 2021

@author: Karl
"""
import spotipy
import config

# Create token
try:
    clientCredentials = spotipy.oauth2.SpotifyClientCredentials(config.clientId, config.clientSecret)
    token = clientCredentials.get_access_token(as_dict = False)
    # Create Spotipy object
    sp = spotipy.Spotify(token)
except:
    print("No Cliend ID or Client Secret Key given or invalid keys.")
    quit()
# Get playlist ID input
playlistIdInput = input("Please enter the spotify playlist URL or URI: ")

# Requires playlist id; Returns a list of track items
def getPlaylistTracks(playlistId):
    # Get first item page
    try:
        results = sp.playlist(playlistId, fields="tracks")
    except:
        print("API-Request Error.")
        return
    # Save current tracks on the page
    tracks = results["tracks"]
    # Save the first page of tracks in a list
    allTracks = tracks['items']
    # While there is a next page
    while tracks['next']:
        # Go forward one page and save the current tracks
        tracks = sp.next(tracks)
        # Extend list with the current tracks
        allTracks.extend(tracks['items'])
    # Return the list of track items
    return allTracks

# Requires a list of track items; Returns the tracklist as string
def getTracklist(allTracks):
    # In case the track item list is empty
    if not allTracks:
        return
    # Create tracklist
    try:
        # Declare tracklist string
        tracklist = ""
        # For every track item in the track item list
        for track in allTracks:
            # Get all artist names
            try:
                # First artist
                artists = track['track']['artists']
                allArtists = ""
                # All other artists
                for artist in artists:
                    if not allArtists:
                        allArtists = artist['name']
                    elif allArtists:
                        allArtists = allArtists + ", " + artist['name']
            # If artist names can't be found
            except:
                allArtists = "ARTIST_ERROR"
            # Track name
            try:
                trackname = track['track']['name']
            # If track name can't be found
            except:
                trackname = "TRACK_ERROR"
            # Write/extend tracklist string
            if not tracklist:
                tracklist = allArtists + " - " + trackname
            elif tracklist:
                tracklist = tracklist + "\n" + allArtists + " - " + trackname
    except:
        print("Something went wrong with the API-Request or reading of the playlist.")
        return
    return tracklist
        
# Get all playlist tracks
tracks = getPlaylistTracks(playlistIdInput)
# Create tracklist
tracklist = getTracklist(tracks)

# Save tracklist in a txt file
try:
    f = open("tracklist.txt", "w", encoding='utf-8')
    f.write(tracklist)
    print("Tracklist successfully created.")
    f.close()
except:
    print("Failed to write the tracklist.txt file.")