"use strict"; //включение "строгого" режима
//События клавиатуры

function checkName(event) {
     console.log(event);
     if (!event.key.match(/[a-zа-я]/i) && event.key.toLowerCase() != 'ё') event.preventDefault(); //запрещаем ввод цифр. Если напечатан цифра, то отменяем печать(действие браузера по умолчанию)
}

function keyup(event) {
    //console.log('key up ' + event.keyCode);
    //console.log('key up ' + event.code);
    console.log('key up ' + event.key);
}

document.addEventListener('DOMContentLoaded', function(event) {
    document.querySelector('input').addEventListener('keydown', checkName);
    document.querySelector('div').addEventListener('keydown', checkName);
    window.addEventListener('keydown', checkName); //слушатель нажатия кнопок по всему окну
    window.addEventListener('keyup', keyup); //слушатель нажатия кнопок по всему окну
});