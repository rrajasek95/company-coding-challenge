
function takeQuiz(quizId) {
    sessionStorage.setItem('user_email', 'test@test.com');
    sessionStorage.setItem('quiz_id', quizId);

    window.location.replace("/quiz_ui");
}

function getAllQuizzes() {
    return fetch('/quizzes').then(response => response.json());
}

(function() {
    getAllQuizzes().then(quizzes => {
        let quizListElement = document.getElementById('quiz_list');
        let quizListString = "";

        for (let i = 0; i < quizzes.length ; i++) {
            let quizId = quizzes[i];

            quizListString += `<li><a href="#" onclick="takeQuiz(${quizId})">Quiz ${quizId}</a></li>\n`;
        }

        quizListElement.innerHTML = quizListString;
    })
})();