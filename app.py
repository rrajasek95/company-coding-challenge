import json

from flask import Flask, render_template

from db import db

app = Flask(__name__, static_url_path='/assets',
            static_folder='assets')

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/quiz')
def get_quiz():
    quiz = db.get_quiz("1")
    return json.dumps(quiz)


@app.route('/quiz/{id}')
def submit_quiz():
    pass

@app.route('/quiz_ui/')
def get_quiz_ui():
    return render_template('quiz.html')