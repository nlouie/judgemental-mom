# app.py
# Judgemental Mom
# CS411 A2 Group 8 Project
# Created by nlouie on 11/1/16
# Last updated by nlouie on 11/6/16
# Description: This is the main app script. Run me to start the server!
#              Initializes the web app and sets up views (routes)


# ------------------ Imports --------------------- #


from flask import Flask, request, render_template, Response, make_response, session, redirect, url_for
from config import load_auth_json

from auth_config import CONFIG     # for authomatic
from authomatic import Authomatic
from authomatic.adapters import WerkzeugAdapter

# JM scripts

from src.analyze import analyze
from src.register import register
from src.connect import extract_facebook

# for testing
from test import test_me
from test2 import test_me2


# ----------------- Init ----------------------------#

# initialize flask
app = Flask(__name__)
app.secret_key = load_auth_json()['flask']['secret_key']
app.config['SESSION_TYPE'] = 'filesystem'
app.config['DEBUG'] = True

# Instantiate Authomatic.
authomatic = Authomatic(CONFIG, 'your secret string', report_errors=False)

# ------------------ Functions ------------------------#

# We'll use this function later to initialise or increment
# a counter that will be stored as a session variable
# This function will be called from every route, so it will
# keep a record of how many routes/pages have been loaded


# ------------------ Routes --------------------------#

# index
@app.route('/')
def hello_world():
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

<<<<<<< Updated upstream
        # first, check if user exists already
        # if not, register the user with result.id
        # else, welcome the user
        # finally, extract info

        output = extract_facebook(result)

=======
        output = extract_facebook(result)

>>>>>>> Stashed changes
        return render_template('login.html', result=result, output=output)

    # Don't forget to return the response.
    return response

# logout


@app.route('/logout', methods=['POST'])
def logout():
    pass


# analyze


@app.route('/analyze')
def view_analyze():
    return render_template('analyze.html')

# connect


@app.route('/connect')
def view_connect():
    return render_template('connect.html')

# Examples for assignment 3 or for reference


# indico mood analysis

@app.route('/test', methods=['GET', 'POST'])
def view_test():
    if request.method == 'POST':
        api_key = load_auth_json()['indico']['api_key']
        response = request.form['input']
        emotion_dict = test_me(response, api_key)
        return render_template('test/test.html', response=emotion_dict)
    else:
        return render_template('test/test.html')

# spotify artist search


@app.route('/test2', methods=['GET', 'POST'])
def view_test2():
    if request.method == 'POST':
        artist_query = request.form['artist']
        response = test_me2(artist_query)
        return render_template('test/test2.html', response=response)
    else:
        return render_template('test/test2.html')

# This route will clear the variable sessions
# This functionality can come handy for example when we logout
# a user from our app and we want to clear its information
@app.route('/clear')
def clearsession():
    # Clear the session
    session.clear()
    # Redirect the user to the main page
    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    # http://flask.pocoo.org/docs/0.11/config/
    app.run()

# eof
