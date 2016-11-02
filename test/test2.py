import json
import requests

def test_me2(input):
    r = requests.get('https://api.spotify.com/v1/search?q='+str(input)+'&type=artist')
    print (r.text)
    return r