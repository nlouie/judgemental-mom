import requests


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
