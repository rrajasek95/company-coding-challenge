import json
import sqlite3

class DB(object):
    """
    Creating a mock database
    """

    quizzes = {
        "1": [
            {
                "text": "Test 123"
            },
            {
                "text": "Test 234"
            },
            {
                "text": "Test 345"
            }
        ]
    }

    responses = {
        "1": {
            "test@test.com": [
                {
                    "response": "Testttt"
                },
                {
                    "response": "Test"
                }
            ]
        }
    }

    def __init__(self, db_url):
        self.db = sqlite3.connect(db_url)

    def get_quiz(self, quiz_id):
        """
        Get the specified quiz
        :param id:
        :return:
        """
        c = self.db.cursor()
        c.execute('''SELECT * FROM questions WHERE quiz_id=?''', quiz_id)
        questions = [{"text": row[0]} for row in c.fetchall()]
        c.close()
        return questions

    def submit_quiz_responses(self, quiz_id, user_id, responses):
        c = self.db.cursor()
        c.execute('''INSERT INTO responses VALUES (?, ?, ?)''', quiz_id, user_id, json.dumps(responses))
        c.close()
        return True

    def get_all_quizzes(self):
        c = self.db.cursor()
        c.execute('''SELECT * FROM quizzes''')
        quizzes = [row[0] for row in c.fetchall()]
        return quizzes

db = DB('quiz.db')