# analyze.py
# Judgemental Mom
# CS411 A2 Group 8 Project
# Created by nlouie on 11/17/16
# Last updated by corey on 11/18/16
# Description: Extracts fb analysis response data, analyzes the data.

import authomatic
from database import add_app_token
from urllib.parse import urlunparse, urlencode
import requests


def init_output():
    output = {'name': "",
              'email': "",
              'oauth_id': "",
              'about': "",
              'religion': "",
              'artist_likes': [],
              'relationship_status': "",
              'posts_data': {},
              'posts_paging': {},
              'likes_data': {},
              'likes_paging': {},
              'political': "",
              'num_friends': "",
              'birthday': "",
              'gender': ""
              }
    return output

def create_fb_request_url(oauth_id):
    # get all the dirt

    # add fb id to base
    base = 'https://graph.facebook.com/{0}'.format(oauth_id) + '?%s'

    fields = ['about',
              'gender',
              'religion',
              'music.limit(10)',
              'relationship_status',
              'posts.limit(100){message,status_type}',
              'email',
              'friends',
              'likes.limit(10)',
              'political',
              'birthday']
    # create the url encoding for 'fields=about,...' by joining the list of fields by a common and encoding.
    params = urlencode({'fields': ','.join(fields)})
    # format %s
    url = base % params
    return url


def extract_facebook_request(output, data):
    # extract data and add to output dictionary
    # important to perform input validation!

    if 'about' in data:
        output['about'] = data.get('about')
    if 'gender' in data:
        output['gender'] = data.get('gender')
    if 'religion' in data:
        output['religion'] = data.get('religion')
    if 'music' in data:
        for artist in data.get('music').get('data'):
            artists = []
            artists += [artist.get('name')]
            output['artists_likes'] = artists
    if 'relationship_status' in data:
        output['relationship_status'] = data.get('relationship_status')
    if 'feed' or 'posts' in data:
        output['posts_data'] = data.get('posts').get('data')
        output['posts_paging'] = data.get('posts').get('paging')  # paging:{previous:"",next:""}
    if 'email' in data:
        output['email'] = data.get('email')
    if 'friends' in data:
        output['num_friends'] = data.get('friends').get('summary').get('total_count')
    if 'likes' in data:
        output['likes_data'] = data.get('likes').get('data')
        # paging:{cursors:{before:"", after:""}, next:""}
        output['likes_paging'] = data.get('likes').get('paging')
    if 'political' in data:
        output['political'] = data.get('political')
    if 'birthday' in data:
        output['birthday'] = data.get('birthday')
    return output


def extract_facebook(result):
    """

    :param result: The Facebook oAuth result
    :return output: dictionary of data
    """
    # https://developers.facebook.com/docs/graph-api/reference/

    # fields
    output = init_output()
    output['name'] = result.user.name
    output['oauth_id'] = oauth_id = result.user.id

    if result.user.credentials:
        if result.provider.name == 'fb':
            url = create_fb_request_url(oauth_id)
            # make the request
            response = result.provider.access(url)
            if response.status == 200:
                if 'error' in response.data:
                    raise Exception("Invalid response: " + response.status)
                output = extract_facebook_request(output, response.data)
        return output
    else:
        raise Exception("Invalid credentials")


def analyze(user_data, indico_api_key):
    results = {}
    # Analyze messages
    results['messages'] = analyze_messages(user_data, indico_api_key)
    return results


def extract_messages_from_posts(posts):
    messages = []
    for post in posts:
        if 'message' in post and 'status_type' in post:
            # some types of posts are not conducive to text analysis.
            if post['status_type'] in {'mobile_status_update', 'added_photos', 'added_video', 'wall_post'}:
                messages += [post['message']]
    return messages


def analyze_messages(user_data, indico_api_key):
    results = {}
    posts_data = user_data.get('posts_data')
    print(posts_data)
    messages = extract_messages_from_posts(posts_data)
    print('messages', messages)
    if len(messages) < 1:
        results['error'] = "Not enough data"
    else:
        print('emotion analysis')
        # make batch emotion anaysis to indicoio

        headers = {'X-ApiKey': str(indico_api_key)}
        data = {'data': messages}
        r = requests.get('https://apiv2.indico.io/emotion/', headers=headers, data=data)
        results['emotion'] = r.json()
    print(results)
    return results

