# spotify.py
# Judgemental Mom
# CS411 A2 Group 8 Project
# Created by nlouie on 11/25/16
# Last updated by nlouie on 12/01/16
# Description: Makes spotify requests. see test2/ for example.
# Resources:
#           https://developer.spotify.com/web-api/get-category/
#           https://developer.spotify.com/web-api/get-categorys-playlists/
#           https://developer.spotify.com/web-api/user-guide/#spotify-uris-and-ids
#           https://developer.spotify.com/web-api/console/get-search-item/?q=%22doom%20metal%22&type=playlist

import requests


def suggest_emotion_playlist(top_mood):
    """
    Suggests a playlist by searching for playlists of that top emotion.

    Expected returned dict:
    {
      "playlists": {
        "href": "...",
        "items": [...],
        "name": "..."

    }

    :param top_mood: str
    :return: dictionary
    """
    # make the api call
    endpoint = 'https://api.spotify.com/v1/search?q=' + str(top_mood) + '&type=playlist&limit=10'
    req = requests.get(endpoint)

    if req.status_code == 200:
        # convert to json
        r_dict = req.json()
        return r_dict
    else:
        return {'error': {'message': 'problem with request'}}

# eof
