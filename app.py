import json
import sqlite3

from flask import Flask, request, render_template, g


app = Flask(__name__, static_url_path='/assets',
            static_folder='assets')

DATABASE = 'quiz.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def hello_world():
    return render_template('startpage.html')

@app.route('/quizzes')
def get_all_quizzes():
    c = get_db().cursor()
    c.execute('''SELECT * FROM quizzes''')
    quizzes = [row[0] for row in c.fetchall()]
    return json.dumps(quizzes)

@app.route('/quiz/<id>', methods=['GET', 'POST'])
def handle_quiz(id):
    if request.method == "GET":
        c = get_db().cursor()
        c.execute('''SELECT text FROM questions WHERE quiz_id=?''', id)
        questions = [{"text": row[0]} for row in c.fetchall()]
        c.close()

        return json.dumps(questions)
    else:
        # Assume POST request and JSON
        submission = request.get_json()
        c = get_db().cursor()
        responses = submission['responses']
        print(submission)
        try:
            c.execute('''REPLACE INTO responses(quiz_id, user_email, responses) VALUES (?, ?, ?)''', (id, submission['user_email'], json.dumps(responses)));
        except sqlite3.Error as e:
            print(e)
        get_db().commit()

        return json.dumps({"submitted": True}), 200


@app.route('/quiz_ui/')
def get_quiz_ui():
    return render_template('quiz.html')

@app.route('/thankyou')
def get_thank_you_page():
    return render_template('thankyou.html')