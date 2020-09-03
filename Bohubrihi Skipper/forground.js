var element = document.getElementsByClassName('sfwd-mark-complete').length;
if (element == 2) {
        const skipButton = document.createElement('button');
        skipButton.innerText = "Skip This Lesson";
        skipButton.id = "skipButton";
        document.querySelector('body').appendChild(skipButton);
}
//document.getElementsByClassName("sfwd-mark-complete")[0].submit();
