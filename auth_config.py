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
        'consumer_key': '1399636540049795',
        'consumer_secret': 'f4bb3abe109d0af37f4d3d064494b907',

        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'user_posts, user_likes']
    }
}