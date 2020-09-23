"use strict"; //включение "строгого" режима
//Базовые события и их обработка

function handlerButton(obj) {
    console.log(obj.innerHTML);
}

function handlerButton2(event) {
    console.log(event.target.innerHTML); //объект target у event содержит элемент, на котором сработало событие
}

function handlerButton3(event) {
    console.log(event.target.innerHTML); //объект target у event содержит элемент, на котором сработало событие
}

document.getElementById('button2').onclick = handlerButton2;
document.getElementById('button3').addEventListener('click', handlerButton3);
document.getElementById('button3').removeEventListener('click', handlerButton3); //удалить событие с элемента

