# Judgemental Mom
# CS411 A2 Group 8 Project
# Created by nlouie on 11/1/16
# Last updated by nlouie on 11/2/16
# Description: This is the main app script. Run me to start the server!

# ------------------ Imports --------------------- #

from flask import Flask, request, render_template, session, Response
from functools import wraps

from src.test.test import test_me
from src.test.test2 import test_me2
import src.login

# ----------------- Init ----------------------------#

app = Flask(__name__)




# ----------------- Basic Authentication ------------------------#

# need a better authentication method..

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

# index
@app.route('/')
def hello_world():
    return render_template('index.html')

# login
@app.route('/login', methods=['GET','POST'])
def view_login():
    if request.method == 'POST':
        username = request.form['username']
        # plz do this better with hashes, this is just an example
        password = request.form['password']
        return render_template('login.html', username=username, password=password)
    else:
        return render_template('login.html')

# logout
@app.route('/logout', methods=['POST'])
def logout():
    pass

# example of requiring authenticationg

@app.route('/account')
@requires_auth
def secret_page():
    return render_template('account.html')

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
        response = request.form['input']
        d = test_me(response)
        return render_template('test/test.html', response=d)
    else:
        return render_template('test/test.html')

# spotify artist search

@app.route('/test2', methods=['GET', 'POST'])
def view_test2():
    if request.method == 'POST':
        input = request.form['artist']
        r = test_me2(input)
        return render_template('test/test2.html', response=r)
    else:
        return render_template('test/test2.html')


if __name__ == '__main__':
    app.run()

# eof
