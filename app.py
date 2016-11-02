from flask import Flask, request, render_template
from test import test_me

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test', methods=['GET','POST'])
def test_call():
    if request.method == 'POST':
        response = request.form['input']
        d = test_me(response)
        return render_template('test.html', response=d)
    else:
        return render_template('test.html')

if __name__ == '__main__':
    app.run()
