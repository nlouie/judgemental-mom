import indicoio
import json

indicoio.config.api_key = json.load(open('auth.json', 'r'))['indico']['api_key']

def test_me(input):
    # single example
    d = indicoio.emotion(input)
    return d