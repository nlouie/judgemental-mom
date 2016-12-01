# app.py
# Judgemental Mom
# CS411 A2 Group 8 Project
# Created by nlouie on 11/1/16
# Last updated by nlouie on 11/6/16
# Description: This is the main app script. Run me to start the server!
#              Initializes the web app and sets up views (routes)


# ------------------ Imports --------------------- #

# very important
from flask import Flask, request, render_template, Response, make_response, session, redirect, url_for
from config import load_auth_json

# for authomatic
from auth_config import CONFIG
from authomatic import Authomatic
from authomatic.adapters import WerkzeugAdapter

# for basic auth
from functools import wraps

# --- JM scripts ---#

from src.analyze import analyze, extract_facebook
from src.register import db_user
from src.spotify import suggest_emotion_playlist

# for testing
from test import test_me
from test2 import test_me2

# database
import user_database

# ----------------- Init ----------------------------#

# initialize flask
app = Flask(__name__)
app.secret_key = load_auth_json()['flask']['secret_key']
app.config['SESSION_TYPE'] = 'filesystem'
app.config['DEBUG'] = True
app.config['FB_KEY'] = load_auth_json()['facebook']['app_secret']
app.config['INDICO_KEY'] = load_auth_json()['indico']['api_key']

# Instantiate Authomatic.
authomatic = Authomatic(CONFIG, 'your secret string', report_errors=False)

# ------------------ Functions ------------------------#


# --------------- Basic Auth is temporary --------------#

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

# ------------------ Routes --------------------------#


@app.route('/')
def hello_world():
    """
    Index page
    :return:
    """
    # Initialise the counter, or increment it
    return render_template('index.html')


# facebook login with authomatic


@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login_oauth(provider_name):
    """
    Login handler, must accept both GET and POST to be able to use OpenID.
    We currently only accept facebook logins
    """

    # We need response object for the WerkzeugAdapter.
    response = make_response()

    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name, session=session,
                              session_saver=lambda: app.save_session(session, response))

    # If there is no LoginResult object, the login procedure is still pending.
    if result:
        if result.user:
            # We need to update the user to get more info.
            result.user.update()

        user_data = extract_facebook(result)
        # handles user database entry
        db_user(user_data)
        user_database.add_app_token(result.user.id, result.user.credentials)
        analysis = analyze(user_data, app.config['INDICO_KEY'])
        playlists_recs = suggest_emotion_playlist(analysis['messages']['emotion'])
        return render_template('login.html', result=result, output=user_data, playlists_recs=playlists_recs)

    # Don't forget to return the response.
    return response


@app.route('/logout', methods=['POST'])
def logout():
    clear_session()


@app.route('/analyze')
def view_analyze():
    """
    Currently unused.
    :return:
    """
    return render_template('analyze.html')


@app.route('/connect')
def view_connect():
    """
    Currently Unused
    :return:
    """
    return render_template('connect.html')


@app.route('/account')
def view_account():
    """
    User account
    :return:
    """
    # todo: figure out sessions
    return render_template('account.html')


@app.route('/admin')
@requires_auth
def admin():
    """
    Admin page
    :return:
    """
    return render_template('admin.html')

# This route will clear the variable sessions
# This functionality can come handy for example when we logout
# a user from our app and we want to clear its information


@app.route('/clear')
def clear_session():
    """
    # Clear the session
    :return:
    """
    session.clear()
    # Redirect the user to the main page
    return redirect(url_for('hello_world'))

# Examples for assignment 3 or for reference


@app.route('/test', methods=['GET', 'POST'])
def view_test():
    """
    # indico mood analysis
    :return:
    """
    if request.method == 'POST':
        api_key = load_auth_json()['indico']['api_key']
        response = request.form['input']
        emotion_dict = test_me(response, api_key)
        return render_template('test/test.html', response=emotion_dict)
    else:
        return render_template('test/test.html')


@app.route('/test2', methods=['GET', 'POST'])
def view_test2():
    """
    # spotify artist search
    :return:
    """
    if request.method == 'POST':
        artist_query = request.form['artist']
        response = test_me2(artist_query)
        return render_template('test/test2.html', response=response)
    else:
        return render_template('test/test2.html')

if __name__ == '__main__':
    # http://flask.pocoo.org/docs/0.11/config/
    app.run()

# eof
