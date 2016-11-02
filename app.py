from flask import Flask, request, render_template
import json

from src.test.test import test_me
from src.test.test2 import test_me2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def view_login():
    if request.method == 'POST':
        username = request.form['username']
        # plz do this better with hashes, this is just an example
        password = request.form['password']
        return render_template('login.html', username=username, password=password)
    else:
        return render_template('login.html')

# Examples

@app.route('/test', methods=['GET','POST'])
def test_call():
    if request.method == 'POST':
        response = request.form['input']
        d = test_me(response)
        return render_template('test/test.html', response=d)
    else:
        return render_template('test/test.html')

@app.route('/test2', methods=['GET', 'POST'])
def test_call2():
    if request.method == 'POST':
        input = request.form['artist']
        r = test_me2(input)
        return render_template('test/test2.html', response=r.text)
    else:
        return render_template('test/test2.html')


if __name__ == '__main__':
    app.run()

# eof
