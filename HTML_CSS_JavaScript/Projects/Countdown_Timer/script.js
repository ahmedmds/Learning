function getTimeRemaining (target_time) {
    var t_remaining = Date.parse(target_time) - Date.parse(new Date());
    var seconds = Math.floor((t_remaining / 1000) % 60);
    var minutes = Math.floor((t_remaining / 1000 / 60) % 60);
    var hours = Math.floor((t_remaining / (1000 * 60 * 60)) % 24);
    var days = Math.floor(t_remaining / (1000 * 60 * 60 * 24));
    return {
        'total': t_remaining,
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
    };
}


function initializeTimer(id, target_time) {
    var timer = document.getElementById(id);
    var daysSpan = timer.querySelector('.days');
    var hoursSpan = timer.querySelector('.hours');
    var minutesSpan = timer.querySelector('.minutes');
    var secondsSpan = timer.querySelector('.seconds');

    function updateTimer() {
        var t_remaining = getTimeRemaining(target_time);

        daysSpan.innerHTML = t_remaining.days;
        hoursSpan.innerHTML = ('0' + t_remaining.hours).slice(-2);
        minutesSpan.innerHTML = ('0' + t_remaining.minutes).slice(-2);
        secondsSpan.innerHTML = ('0' + t_remaining.seconds).slice(-2);

        if (t_remaining.total <= 0) {
            clearInterval(timeinterval);
        }
    }

    updateTimer();
    var timeinterval = setInterval(updateTimer, 1000); // Timer updated every 1000 milliseconds
}

var currentYear = new Date()
var deadline = currentYear.getFullYear() + 1 + '-01-01'; // Next New Year Date
// var deadline = new Date(Date.parse(new Date()) + 7 * 24 * 60 * 60 * 1000); // One week later from now
// var deadline = '2030-01-14'; // Arbitrary date
initializeTimer('timerdiv', deadline);