from flask_oauth import OAuth
from flask import session
import json


oauth = OAuth()

def get_facebook():
    return oauth.remote_app('facebook', base_url='https://graph.facebook.com.',
                            request_token_url=None,
                            access_token_url='/oauth/access_token',
                            authorize_url='https://www.facebook.com/dialog/oauth',
                            consumer_key=json.load(open('auth.json', 'r'))['facebook']['app_id'],
                            consumer_secret=json.load(open('auth.json', 'r'))['facebook']['app_secret'],
                            request_token_params={'scope': 'email'}
                            )


def get_facebook_token(token=None):
    return session.get('facebook_token')


