
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
            "1": [
                {
                    "response": "Testttt"
                },
                {
                    "response": "Test"
                }
            ]
        }
    }

    def get_quiz(self, quiz_id):
        """
        Get the specified quiz
        :param id:
        :return:
        """
        return DB.quizzes.get(quiz_id)

    def submit_quiz_responses(self, quiz_id, user_id, responses):
        quiz = DB.responses.get(id)
        quiz[user_id] = responses

        return True


db = DB()