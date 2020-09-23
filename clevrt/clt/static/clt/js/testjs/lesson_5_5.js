"use strict"; //включение "строгого" режима
//работа со стилями элементов

let h1 = document.querySelector('#header');

h1.style.fontSize = '100%';
h1.style['color'] = 'red';


function hide() {
    let opacity = Number(Number(document.body.style.opacity).toFixed(2));
    opacity = Number(Number(opacity - 0.01).toFixed(2));
    if (opacity <= 0) {
        opacity = 0;
        show();
    };

    document.body.style['opacity'] = opacity;
    console.log(opacity);
    if (opacity > 0) setTimeout(hide, 10);
}

function show() {
    let opacity = Number(Number(document.body.style.opacity).toFixed(2));
    opacity = Number(Number(opacity + 0.01).toFixed(2));
    if (opacity >= 1) {
        opacity = 1;
        hide();
    };

    document.body.style['opacity'] = opacity;
    console.log(opacity);
    if (opacity < 1) setTimeout(show, 10);
}

document.body.style['opacity'] = '1';
//hide();