import json

def load_json():
    data = json.load(open('auth.json', 'r'))
    return data


