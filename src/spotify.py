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
from json import load

def get_params():
    return load(open('auth.json', 'r'))
    
PARAMS = get_params()

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
    endpoint = 'https://api.spotify.com/v1/search?q=' + str(top_mood) + '&type=playlist&limit=4'
    req = requests.get(endpoint)

    if req.status_code == 200:
        # convert to json
        r_dict = req.json()
        return r_dict
    else:
        return {'error': {'message': 'problem with request'}}

def get_new_access_token():
    """
    get a new access token from spotify to run recommendation API
    
    :return: str
    """
    client_id = PARAMS['spotify']['client_id']
    client_secret = PARAMS['spotify']['client_secret']
    
    data = {'grant_type' : 'client_credentials'}
    url = 'https://accounts.spotify.com/api/token'
    
    req = requests.post(url, data=data, auth=(client_id, client_secret)) 
    
    return req.json()['access_token']

def recommend(user_data, n):
    """
    take FB data and produce intelligent song choices using spotify
    random walk API
    
    :param user_data: dict
    :param n: int
    :return: dict
    """
    headers = {'Authorization': 'Bearer ' + get_new_access_token()}
    
    params = dict(target_acousticness=None, # 0 to 1, float
                  target_danceability=None, # 0 to 1, float
                  target_energy=None, # 0 to 1, float
                  target_populatiry=None, # 0 to 100, float
                  target_valence=None,
                  genre=None)
    
    # important values
    v = {}
    
    for key in user_data['messages']:
        for key2 in user_data['messages'][key]['results']:
            v[key2.lower()] = user_data['messages'][key]['results'][key2]
    for key in user_data['tops']:
        v[key.lower()] = user_data['tops'][key]
    
    # genre
    if v['emotion'] == 'anger':
        params['genre'] = 'edm,grunge,heavy-metal,punk-rock,hard-rock'
    elif v['emotion'] in ['joy', 'surprise']:
        params['genre'] = 'acoustic,ambient,songwriter,soul'
    else:
        params['genre'] = 'alternative,ambient,blues,hard-rock,soul'
        
    # other things
    params['target_valence'] = min(1, v['joy'] + .5*v['surprise'])
    params['target_popularity'] = int(max(.2, 1 - v['libertarian'] - .4*v['green']) * 100)
    params['target_acousticness'] = min(.8, (v['agreeableness'] + v['conscientiousness']) / 1.5)
    params['target_danceability'] = max(0, params['target_valence']*v['extraversion'])
    
    extra = ''
    for key in params:
        if key == 'genre':
            extra += '&seed_genres=' + params[key]
        elif key == 'target_popularity':
            extra += '&target_popularity=' + str(params[key])
        elif params[key] != None:
            extra += '&%s=%.3f' % (key, params[key])
        else:
            pass
        
    
    # EDIT PARAMS BASED ON USER_DATA
    
    base_url = 'https://api.spotify.com/v1/recommendations?market=US&limit=%d' % n
    url = base_url + extra
    
    
    # make spotify request              
    req = requests.get(url, headers=headers).json()
    
    # build dict with songs
    songs = {}
    
    for song in req['tracks']:
        songs[song['name']]={'artist_name': song['artists'][0]['name'], \
                             'artist_spotify_url': song['artists'][0]['external_urls']['spotify'], \
                             'song_preview_url': song['preview_url'], \
                             'album_name': song['album']['name'], \
                             'album_spotify_url': song['album']['external_urls']['spotify'], \
                             'album_preview_pic': song['album']['images'][0]['url'], \
                             'song_spotify_url': song['external_urls']['spotify']}
        
    return songs