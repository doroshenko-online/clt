"use strict"; //включение "строгого" режима
//управление атрибутами элемента

let element = document.querySelector('h1');

console.log(element.hasAttribute('data-id'));
console.log(element.getAttribute('data-id'));

element.setAttribute('data-id', 5);
console.log(element.getAttribute('data-id'));

element.removeAttribute('data-id');
console.log(element.hasAttribute('data-id'));

for (let attr of document.querySelector('h1.title').attributes) {
    console.log(attr);
}

let elements = document.querySelectorAll('a');

for (let e of elements) {
    e.setAttribute('target', 'blank')
}

document.querySelector('h1').classList.add('big'); // получение списка класса и добавление к нему нового класса