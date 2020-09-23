"use strict"; //включение "строгого" режима
let a = prompt('Введите первое число');
let b = prompt('Введите второе число');

a = +a;
b = +b;

if (Number.isNaN(a)) alert('Некоректное первое число');
else if (Number.isNaN(b)) alert('Некорректное второе число');
else {
	alert('Sum: ' + (a + b));
	//let bool = confirm("Хотите узнать их произведение?")
	//if (bool) alert('Multiply: ' + (a * b));
	
	//same
	if (confirm("Хотите узнать их произведение?")) alert('Multiply: ' + (a * b));
}