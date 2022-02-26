var questions = [{
    question: "What is the capital of Germany?",
    choices: ["London", "Berlin", "New York", "Paris"],
    correctAnswer: 1
},
{
    question: "Which continent has the least population?",
    choices: ["Asia", "Europe", "North America", "Antarctica"],
    correctAnswer: 3
},
{
    question: "What is the largest country by area?",
    choices: ["USA", "Brazil", "Russia", "Canada"],
    correctAnswer: 2
},
{
    question: "What is the capital of Spain?",
    choices: ["Madrid", "Barcelona", "Seville", "Valencia"],
    correctAnswer: 0
},
{
    question: "What is the second largest country by area?",
    choices: ["China", "Brazil", "Canada", "USA"],
    correctAnswer: 2
}];


var currentQuestion = 0;
var correctAnswers = 0;
var quizOver = false;


$(document).ready(function() {
    displayCurrentQuestion();
    $(this).find(".quizMessage").hide();
    $(this).find(".nextButton").on("click", function() {
        if (!quizOver) {
            value = $("input[type='radio']:checked").val();
            if (value==undefined) {
                $(document).find(".quizMessage").text("Please select an option");
                $(document).find(".quizMessage").show();
            } else {
                $(document).find(".quizMessage").hide();
                if (value==questions[currentQuestion].correctAnswer) {
                    correctAnswers++;
                }
                currentQuestion++;
                if (currentQuestion < questions.length) {
                    displayCurrentQuestion();
                } else {
                    displayScore();
                    $(document).find(".nextButton").text("Attempt again?");
                    quizOver = true;
                }
            }
        } else {
            quizOver = false;
            $(document).find(".nextButton").text("Next question");
            resetQuiz();
            displayCurrentQuestion();
            hideScore();
        }

    });

});

function displayCurrentQuestion() {
    
    console.log("In display current question");

    var question = questions[currentQuestion].question;
    var questionClass = $(document).find(".quizContainer > .question");
    var choiceList = $(document).find(".quizContainer > .choiceList");
    var numChoices = questions[currentQuestion].choices.length;

    // Set the questionClass text to the current question
    $(questionClass).text(question);

    // Remove all current <li> elements (if any)
    $(choiceList).find("li").remove();

    var choice;
    for (i = 0; i < numChoices; i++) {
        choice = questions[currentQuestion].choices[i];
        $('<li><input type="radio" value=' + i + ' name="dynradio" />' + choice + '</li>').appendTo(choiceList);
    }
}

function resetQuiz() {
    currentQuestion = 0;
    correctAnswers = 0;
    hideScore();
}

function displayScore() {
    $(document).find(".quizContainer > .result").text("You scored: " + correctAnswers + " out of: " + questions.length);
    $(document).find(".quizContainer > .result").show();
}

function hideScore() {
    $(document).find(".result").hide();
}
