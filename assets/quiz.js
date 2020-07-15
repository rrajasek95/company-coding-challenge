function getQuestions(quizId) {
    return fetch(`/quiz/${quizId}`)
        .then(response => {
            return response.json()
        });
}

let timer = {
    "defaultTime": 10,
    "internalTimer": null,
    "onCompletion": null,
    "initialize": function (onCompletionCallback) {
        var that = this;
        this.remainingTime = this.defaultTime;
        this.timerElement = document.getElementById('time_span');
        this.internalTimer = setInterval(() => that.tick(), 1000);
        this.onCompletion = onCompletionCallback;
    },

    "tick": function() {
        if (this.remainingTime === 0) {
            this.onCompletion();
            clearInterval(this.internalTimer);
        }
        this.remainingTime -= 1;

        let minutes = Math.floor(this.remainingTime / 60);
        let seconds = this.remainingTime % 60;
        let minutesStr = "0" + minutes.toString();
        let secondsStr = (seconds < 10 ? "0" : "") + seconds.toString();

        this.timerElement.innerHTML = minutesStr + ":" + secondsStr;
    },
    "clear": function() {
        clearInterval(this.internalTimer);
    },
    "timerElement": null,
};


function getQuizManager(questions, userEmail) {
    return {
        "userEmail": userEmail,
        "questions": questions,
        "responses": [],
        "currentIndex": -1,
        "renderQuestionInUi": function(question, currentIndex) {
            let questionIndexElement = document.getElementById('question_id');
            // Render question i of n
            questionIndexElement.innerHTML = `${(currentIndex + 1)} of ${this.questions.length}`;

            let questionTextElement = document.getElementById('question_text');
            questionTextElement.innerHTML = question.text;
            timer.initialize(() => this.advanceQuestion());
        },
        "advanceQuestion": function() {
            if (this.currentIndex > -1) {
                // Add current response to list of responses
                let response = document.getElementById('response').value;
                this.responses.push(response);
            }

            this.currentIndex += 1;

            if (this.currentIndex === questions.length) {
                this.completeQuiz();

            } else {
                this.renderQuestionInUi(questions[this.currentIndex], this.currentIndex);
            }
        },
        "submitAllResponses": function() {
            // Send a POST request
            return fetch('/quiz/1', {
                "method": 'POST',
                "body": JSON.stringify({
                    "user_email": this.userEmail,
                    "responses": this.responses
                }),
                'headers': {
                    'Content-type': 'application/json; charset=UTF-8'
                }
            });
        },
        "completeQuiz": function() {
            // We have exhausted all questions, now submit the response
            timer.clear();
            this.submitAllResponses().then(() => {
                window.location.replace("/thankyou");
            });
        },
        "startQuiz": function () {
            this.advanceQuestion();
        }
    }
}

(function() {
    let userEmail = window.sessionStorage.getItem('user_email');
    let quizId = window.sessionStorage.getItem('quiz_id');
    getQuestions(quizId).then(questions => {
        let manager = getQuizManager(questions, userEmail);
        let submitButton = document.getElementById('submit');
        submitButton.addEventListener('click', () => manager.advanceQuestion());
        manager.startQuiz();
    });

})();