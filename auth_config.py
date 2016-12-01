from authomatic.providers import oauth2, oauth1
from authomatic import provider_id
from config import load_auth_json

CONFIG = {
    'fb': {

        'class_': oauth2.Facebook,
        'id': provider_id(),

        # Facebook is an AuthorizationProvider too.
        'consumer_key': load_auth_json()['facebook']['app_id'],
        'consumer_secret': load_auth_json()['facebook']['app_secret'],

        # But it is also an OAuth 2.0 provider and it needs scope.
        # https://developers.facebook.com/docs/facebook-login/permissions
        'scope': ['public_profile', 'user_friends', 'user_about_me', 'email', 'user_posts, user_likes',
                  'user_actions.music', 'user_relationships', 'user_religion_politics', 'user_education_history',
                  'user_birthday']
    }
}
