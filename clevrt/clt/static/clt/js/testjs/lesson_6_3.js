"use strict"; //включение "строгого" режима
//Браузерные события и их обработка

//Подтверждение перехода
function myClick() {
    return confirm('You sure?');
}

function clickLink(event) {
    event.preventDefault(); //отменяет стандартную браузерную обработку
    console.log('Click on link: ' + event.target);
}

document.addEventListener('DOMContentLoaded', function (event) { //DOMContentLoaded - ивент загрузки страницы
    console.log('Document was  loaded');
    for (let a of document.querySelectorAll('a')) {
        if (!a.onclick) {
            a.addEventListener('click', clickLink);
        }
    }
});