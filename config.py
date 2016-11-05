import json

def load_json(key):
    data = json.load(open('config.json', 'r'))
    return json.load(open(data[key], 'r'))