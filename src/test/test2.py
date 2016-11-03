import json
import requests


def test_me2(input):

    """
    Takes the artist search query from /test2 and returns a list of all the artists.
    :param input: string
    :return artists: list

    """

    # make the api call
    r = requests.get('https://api.spotify.com/v1/search?q='+str(input)+'&type=artist')

    # convert to json
    r_dict = r.json()

    # extract artists
    artists = r_dict['artists']['items']

    return artists

# eof
