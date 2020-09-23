"use strict"; //включение "строгого" режима
//Добавление и удаление элементов

let p = document.createElement('p');
p.innerHTML = 'Эта строка добавлена через <strong>JavaScript</strong>';
p.setAttribute('class', 'big') //добавление класса
document.body.append(p); //добавление элемента в самом конце
//document.body.prepend(p); //добавление элемента в начале

document.querySelector('ul').before(p); //добавляет радом с выбранным элементом
document.querySelector('ul').after(p.outerHTML); //добавляет радом с выбранным элементом

document.querySelector('ul').insertAdjacentHTML('beforebegin', '<li style="color: red;">Вставка</li>')
document.querySelector('ul').insertAdjacentHTML('beforeend', '<li style="color: red;">Вставка</li>')
document.querySelector('ul').insertAdjacentHTML('afterend', '<li style="color: red;">Вставка</li>')
document.querySelector('ul').insertAdjacentHTML('afterbegin', '<li style="color: red;">Вставка</li>')

//delete
document.querySelector('a').remove();

//copy and add
let ul = document.querySelector('ul').cloneNode(true); //true - копирует вместе с дочерними элементами, false - копирует только сам выбранный элемент

document.body.append(ul);