# test2.py
# Judgemental Mom
# CS411 A2 Group 8 Project
# Created by nlouie on 11/1/16
# Last updated by nlouie on 11/6/16
# Description:

# ------------------ Imports --------------------- #

import requests


# ------------------ Function --------------------- #

def test_me2(artist):
    """
    Takes the artist search query and returns a list of all the artists.
    :param artist: string
    :return artists: list
    """

    # make the api call
    endpoint = 'https://api.spotify.com/v1/search?q=' + str(artist) + '&type=artist'
    req = requests.get(endpoint)

    # convert to json
    r_dict = req.json()

    # extract artists
    artists = r_dict['artists']['items']

    return artists

# eof
