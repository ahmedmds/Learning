// Global document, window, localStorage

// Heading text 'Beautiful View'

var myHeading = document.querySelector('h1');
myHeading.textContent = 'Beautiful View';


// Code for click event

document.querySelector('html').onclick = function() {
    alert('You clicked just now!');
}

// document.querySelector('h1').onclick = function() {
//     alert('You clicked on heading just now!');
// };


// Code for image change

var displayedImage = document.querySelector('img');
displayedImage.onclick = function() {
    var currentImage = displayedImage.getAttribute('src');
    if(currentImage === 'images/image1.jpg') {
        displayedImage.setAttribute('src', 'images/image2.jpg');
    } else {
        displayedImage.setAttribute ('src', 'images/image1.jpg');
    }
};


// Personalised welcome message code

var nameButton = document.querySelector('button');
var myHeading = document.querySelector('h1');

function setUserName() {
    var myName = window.prompt('Please enter a name.');
    localStorage.setItem('name', myName);
    myHeading.textContent = myHeading.textContent + ', ' + storedName;
}
if (!localStorage.getItem('name')) {
    setUserName();
} else {
    var storedName = localStorage.getItem('name');
    myHeading.textContent = myHeading.textContent + ', ' + storedName; 
}

nameButton.onclick = function() {
    setUserName();
};
