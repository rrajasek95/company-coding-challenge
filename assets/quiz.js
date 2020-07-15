
function updateTimer() {

}

function getQuestions() {
    return fetch('/quiz')
        .then(response => {
            return response.json()
        });
}

let timer = {
    "defaultTime": 180,
    "remainingTime": 180,
    "internalTimer": null,
    "initialize": function () {
        var that = this;
        this.remainingTime = this.defaultTime;
        this.timerElement = document.getElementById('time_span')
        this.internalTimer = setInterval(() => that.tick(), 1000);
    },

    "tick": function() {
        if (this.remainingTime == 0) {
            // Logic to advance to next question
            clearInterval(this.internalTimer);
            return;
        }
        this.remainingTime -= 1;

        let minutes = Math.floor(this.remainingTime / 60);
        let seconds = this.remainingTime % 60;
        let minutesStr = "0" + minutes.toString();
        let secondsStr = (seconds < 10 ? "0" : "") + seconds.toString();

        this.timerElement.innerHTML = minutesStr + ":" + secondsStr;
    },

    "timerElement": null,

};

function renderQuestionInUi(question) {
    let questionTextElement = document.getElementById('question_text');
    questionTextElement.innerHTML = question.text;

    timer.initialize();
}

function submitResponse() {
    let quizResponse= document.getElementById('response').value;
}

(function() {
    getQuestions().then(questions => {
        renderQuestionInUi(questions[0]);
    });

})();