"use strict"; //включение "строгого" режима
//доступ к элементу

let header = document.getElementById('header');
header.innerHTML = 'Новый заголовок'

let elements = document.querySelectorAll('li');
//same for our li
elements = document.getElementsByClassName('pi');

for (let ib of elements) {
    console.log(ib);
    ib.style.color = '#0c0'; //смена стилей элемента
    console.log(ib.closest(".test").nodeName) //closest ищет элемент выше по иерархии
}

console.log(document.querySelector('.test').nodeName);