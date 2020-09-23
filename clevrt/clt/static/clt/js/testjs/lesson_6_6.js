"use strict"; //включение "строгого" режима
//События на элементах формы

function handlerFocus(event) {
    if (event.type == 'focus') {
        console.log('Focus on element ' + event.target);
    } else  if (event.type == 'blur') {
        console.log('Unfocus element ' + event.target);
    }
}

function submit(event) {
    console.log('Try to send form');
    let form = event.target;
    let error = document.querySelector('#error');
    error.innerHTML = '';
    let name = form.querySelector('input[name="name"]');
    if (name.value.length == 0) {
        error.innerHTML += 'Empty input<br />';
        name.focus(); //вызов фокуса у эле
    }
    if (!form.querySelector('input[name="rules"]').checked) {
        error.innerHTML += 'Not accept rulse <br />';
    }
    if (error.innerHTML) {
        error.style.display = "inline";
        event.preventDefault(); //отмена отправки формы
    }

}

document.addEventListener('DOMContentLoaded', function (event) {
    document.querySelector('form').addEventListener('submit', submit);
    document.querySelector('input[name="rules"]').addEventListener('focus', handlerFocus); //фокус на элементе
    document.querySelector('input[name="rules"]').addEventListener('blur', handlerFocus); //снятие фокуса
});