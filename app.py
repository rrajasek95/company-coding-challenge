from flask import Flask, render_template

from db import db

app = Flask(__name__, static_url_path='/assets',
            static_folder='assets')

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/quiz/{id}')
def get_quiz():
    return 'Test'


@app.route('/quiz/{id}')
def submit_quiz():
    pass

@app.route('/quiz_ui/')
def get_quiz_ui():
    return render_template('quiz.html')

@app.route('/assets/<path:path>')
def send_asset(path):
    return send_fom_directory('assets', path)