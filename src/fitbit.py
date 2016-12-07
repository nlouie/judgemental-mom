"""
fitbit.py
BU EC521 Fall 2016
Project Group 3
nlouie@bu.edu

This script takes the authorized fitbit user code and scrapes the user's data by making a series of GET requests.
This is *proof of concept* of various data one could take from a fitbit account.

An added proof would be to host this script, but may be against Fitbit API's TOS.

User clicks below link and authorizes, the user is directected with a code in the get request with which the server uses
to make a post request to authorize the app. Fitbit responds to the post request with the user's access and refresh token.
After that, the server now has access to the user's data.

Works only for authorization code flow!

Usage:

Follow the below Authorization URL, login to your Fitbit account, and copy the in your URL header after it redirects you:

https://www.fitbit.com/oauth2/authorize?response_type=code&client_id=228349&redirect_uri=https%3A%2F%2Fjudgementalmom.com%2Ffitbit&scope=activity%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in=604800

or make a curl

$ curl -X POST -i -H 'Authorization: Basic MjI4MzQ5OjdkMzJmMDMwNzRhMmQ5ODJkNjM3ZjhhYjFhZjBiNmZl' -H 'Content-Type: application/x-www-form-urlencoded' -d "clientId=228349" -d "grant_type=authorization_code" -d "redirect_uri=https%3A%2F%2Fjudgementalmom.com%2Ffitbit" -d "code=0716ea988383f3c400e21adbfe70902293218dcc" https://api.fitbit.com/oauth2/token

The authorization links to my shared hosting, but will return a 500 error. Look at your URL header to see your code!!!

This is for use by Team members only.
If you would like to use this for your own Fitbit app, simply replace your authorization code in global_headers,
and your redirect_uri in oauth_request_data.

When you run this, you are using this script at your own discretion. We hold no warranty for this script. If you are not
redirecting to a secure server (if no https), then you may expose your sensitive information as this app requests for
a maximum amount of informational access to your fitbit account. You should never use this on anyone's account you
do not have permission to use.

More info about authentication: https://dev.fitbit.com/docs/oauth2/


Production link:

https://www.fitbit.com/oauth2/authorize?response_type=code&client_id=228349&redirect_uri=http%3A%2F%2F45.55.134.62%3A5000%2Ffitbit&scope=activity%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in=604800


"""

user_code = ""
fitbit_secret = ""
fitbit_authorization = "Basic MjI4MzQ5OjdkMzJmMDMwNzRhMmQ5ODJkNjM3ZjhhYjFhZjBiNmZl"
fitbit_client_id = "228349"

# -------------------- IMPORTS --------------------------------------------#

import requests
from json import load, dumps


# --------------------- GLOBALS --------------------------------------------#

# Build authentication POST

# final extracted returned data
FINAL_OUTPUT = {}

# Use this URL to refresh the access token
TOKEN_URL = "https://api.fitbit.com/oauth2/token"

global_headers = {
    'Authorization': fitbit_authorization,
    'Content-Type': 'application/x-www-form-urlencoded',
}



# All the api endpoints for extraction of user data. note that we are using a static date, 2016-10-30 for proof
# of concept and simplicity, but one could obtain the date the user signed up and request the range between then and
# now in order to obtain all the user's data.
# It's important to note that the [user-id] area of the url must be replaced with {0} in order to be compatible with the
# string formatting done in getData().
# By adding the name and api endpoint url, the extraction function will automatically extract the user's data from the
# provided endpoint
EXTRACTION_URLS = {
    'user_data': 'https://api.fitbit.com/1/user/{0}/profile.json',
    'body_data': 'https://api.fitbit.com/1/user/{0}/body/log/fat/date/2016-12-02.json',
    'devices_data': 'https://api.fitbit.com/1/user/{0}/devices.json',
    'weight_data': 'https://api.fitbit.com/1/user/{0}/body/log/weight/date/2016-12-02.json',
    'food_data': 'https://api.fitbit.com/1/user/{0}/foods/log/date/2016-12-02.json',
    'friends_data': 'https://api.fitbit.com/1/user/{0}/friends.json',
    'sleep_data': 'https://api.fitbit.com/1/user/{0}/sleep/date/2016-12-02.json',
    'heart_data': 'https://api.fitbit.com/1/user/{0}/activities/heart/date/today/1d.json'
}

# ----------------- FUNCTIONS --------------------------------------------#


def get_auth_url():
    url = "https://www.fitbit.com/oauth2/authorize?response_type=code&client_id=228349&redirect_uri=http%3A%2F%2F45.55.134.62%3A5000%2Ffitbit&scope=activity%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in=604800"
    return url

def get_new_access_token(refresh_token):
    """
    after using an access token, we must request another one using the refresh token that we already have.
    :param refresh_token: str ref
    :return: str, str
    """
    data = {'grant_type': 'refresh_token',
            'refresh_token': refresh_token}
    r = requests.post(TOKEN_URL, headers=global_headers, data=data)
    access_token = r.json()['access_token']
    refresh_token = r.json()['refresh_token']
    return access_token, refresh_token


def get_data(url, user_id, headers, data, name):
    """
    Makes the request and puts it into the final output
    :param url: api endpoint
    :param user_id: fitbit user id
    :param headers: header with a fresh access token
    :param data: should be empty dictionary
    :param name: name of data as defined in EXTRACTION_URLS keys
    :return: None
    """
    r = requests.get(url.format(user_id), headers=headers, data=data)
    if r.status_code is 200 and 'errors' not in r.json():
        FINAL_OUTPUT[name] = r.json()


def extract(access_token, refresh_token, user_id):
    """
    Sets up the url requests, calls get_data()
    :param access_token: fresh access token
    :param refresh_token: fresh refresh token
    :param user_id: fitbit user id
    :return: None
    """
    # default headers and data
    headers = {'Authorization': 'Bearer ' + str(access_token)}
    data = {}
    # Make a call for each API endpoint
    for key in EXTRACTION_URLS:
        print("\textracting " + str(key) + "...")
        # set up the request
        url = EXTRACTION_URLS[key]
        # make the request
        get_data(url, user_id, headers, data, name=key)
        # reset
        # refresh the token and refresh the headers
        access_token, refresh_token = get_new_access_token(refresh_token)
        headers = {'Authorization': 'Bearer ' + str(access_token)}


def extract_fitbit(CODE):
    """
    Bottom method.
    :return: -o output.txt by default.
    """

    redirect_url = "http://45.55.134.62:5000/fitbit"
    # redirect_url = 'https://judgementalmom.com/fitbit'

    oauth_request_data = {
        'clientId': fitbit_client_id,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_url,
        'code': CODE
    }

    print("Authenticating...\n")
    r = requests.post(TOKEN_URL, headers=global_headers, data=oauth_request_data)
    oauth_data = r.json()
    if 'errors' not in oauth_data:
        access_token = oauth_data['access_token']
        user_id = oauth_data['user_id']
        refresh_token = oauth_data['refresh_token']
        print("Extracting...\n")
        extract(access_token, refresh_token, user_id)
        print(dumps(FINAL_OUTPUT, sort_keys=True, indent=4))
        # output to text..
        print("Output: ------------------------------------------------\n")
        with open('output.txt', 'w') as f:
            f.write(str(dumps(FINAL_OUTPUT, sort_keys=True, indent=4)))
    else:
        print('error in oauth', oauth_data)



def run_fibit(code, secret):
    user_code = code
    fitbit_secret = secret
    # fitbit_authorization = authorization
    extract_fitbit(code)