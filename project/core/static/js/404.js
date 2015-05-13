(function () {
    'use strict';
    window.AX = window.AX || {};
    var robotSaysText = "Sorry could not generate this content :(";
    var robotsTextElem = document.getElementById("robot-says");
    window.AX.robotTypes = function(robotsTextElem, robotSaysText, robotSaysTextLenght) {
        (function robotWriter(charIndex) {

            var typingInterval = Math.floor(Math.random() * (50) + 50);
            charIndex++;
            robotsTextElem.innerHTML = robotSaysText.substring(0, charIndex);

            if ( robotSaysTextLenght >= charIndex) {
                setTimeout(function() {
                    robotWriter(charIndex);
                }, typingInterval);
            }
        })(0);
    };

    AX.robotTypes(robotsTextElem, robotSaysText, robotSaysText.length);
})();