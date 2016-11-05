from authomatic.providers import oauth2, oauth1
from config import load_json

CONFIG = {

    'tw': {  # Your internal provider name

        # Provider class
        'class_': oauth1.Twitter,

        # Twitter is an AuthorizationProvider so we need to set several other properties too:
        'consumer_key': '########################',
        'consumer_secret': '########################',
    },

    'fb': {

        'class_': oauth2.Facebook,

        # Facebook is an AuthorizationProvider too.
        'consumer_key': load_json()['facebook']['app_id'],
        'consumer_secret': load_json()['facebook']['app_secret'],

        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'user_posts, user_likes']
    }
}