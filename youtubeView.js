// window.location.reload(true);
// reload the page
// Math.floor(Math.random()*6);
// random number genarator
// let t = Math.floor(Math.random() * (max - min) ) + min;
min = 1;
max = 4;
for (i=1; i<10000; i) {
    let t = Math.floor(Math.random() * (max - min) ) + min;
    setTimeout(function() {
        window.location.reload(true);
   }, 60000 * t);
} 