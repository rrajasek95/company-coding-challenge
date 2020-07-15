import json

from flask import Flask, request, render_template

from db import db

app = Flask(__name__, static_url_path='/assets',
            static_folder='assets')

@app.route('/')
def hello_world():
    return render_template('startpage.html')

@app.route('/quizzes')
def get_all_quizzes():
    return json.dumps(db.get_all_quizzes())

@app.route('/quiz/<id>', methods=['GET', 'POST'])
def handle_quiz(id):
    if request.method == "GET":
        quiz = db.get_quiz(id)
        return json.dumps(quiz)
    else:
        # Assume POST request and JSON
        submission = request.get_json()
        db.submit_quiz_responses(id, submission['user_email'], submission['responses'])
        return json.dumps({"submitted": True}), 200


@app.route('/quiz_ui/')
def get_quiz_ui():
    return render_template('quiz.html')

@app.route('/thankyou')
def get_thank_you_page():
    return render_template('thankyou.html')