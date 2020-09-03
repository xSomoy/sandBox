function check() {
    var element = document.getElementsByClassName('sfwd-mark-complete').length;
    if (element == 2) {
        const skipButton = document.createElement('button');
        skipButton.innerText = "Skip This Lesson";
        skipButton.id = "skipButton";
        document.querySelector('body').appendChild(skipButton);
        skipButton.addEventListener("click", skip);
        console.log('aloha');
    }
};
setInterval(check, 500);

function skip() {
    document.getElementsByClassName("sfwd-mark-complete")[0].submit();
};
