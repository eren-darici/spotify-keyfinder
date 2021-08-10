from SpotifyAPIManager import Spotify
import json

spotifyManager = Spotify()

spotifyManager.login()

spotifyManager.currentSong('tonal_information.json')
