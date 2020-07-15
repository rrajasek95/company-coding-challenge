from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/quiz/{id}')
def get_quiz():
    return 'Test'


@app.route('/quiz/{id}')
def submit_quiz():
    pass