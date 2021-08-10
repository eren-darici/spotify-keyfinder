from flask import Flask, render_template, url_for
from SpotifyAPIManager import Spotify
from spotipy.cache_handler import CacheFileHandler
import json
import os

app = Flask(__name__)
spotifyManager = Spotify()


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/currentSong')
def main():
    if os.path.exists(".cache"):
        delete_cache()
    else:
        spotifyManager.login()
        cacheHandler = CacheFileHandler()
        with open('cache.json', 'w+') as json_file:
            json.dump(cacheHandler.get_cached_token(), json_file, indent=4)
        data = spotifyManager.currentSong('tonal_information.json')
        print(data)

        key_info = """Key: {} {}""".format(data['key'], data['mode'])

        tempo = "Tempo: {}".format(data['tempo'])

        spotifyManager.download_cover(data['cover_url'])
        print(data['cover_url'])

        try:
            delete_cache()
        except:
            print("ERROR: No cache file found")
        finally:
            return render_template('current_song.html', name=data['song'], artist=data['artist'], info=key_info, tempo=tempo)

def delete_cache():
    file = '.cache'
    path = os.path.join(os.getcwd(), file)
    os.remove(path)


if __name__ == '__main__':
    app.run()
