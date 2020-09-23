"use strict"; //включение "строгого" режима
//События мыши

function mouseover(event) {
    console.log('Mouse on event: ' + event.target);
}
function mouseout(event) {
    console.log('Mouse left from event: ' + event.target);
}

function mousemove(event) {
    console.log('Mouse over object: ' + event.x + "; " + event.y);
}

function mousedown(event) {
    console.log('click on object: ' + event.target);
}

function mouseup(event) {
    console.log('отпустили мышь on object: ' + event.target);
}

let div = document.querySelector('div');
div.addEventListener('mouseover', mouseover);
div.addEventListener('mouseout', mouseout);
div.addEventListener('mousemove', mousemove);
div.addEventListener('mousedown', mousedown); //нажатие мыши
div.addEventListener('mouseup', mouseup); //отпускание мыши
window.addEventListener('scroll', function(event){ //scroll event
    console.log('scroll');
    console.log('Move ' + window.pageYOffset);
});