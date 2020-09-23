"use strict"; //включение "строгого" режима
function hello() {
		console.log("Выводим в консоль");
}

console.log(hello);

let h = function(){
	console.log("Функциональное выражение");
}

let f = hello;

f();
h();
console.log(h);

function success(name) {
	alert(`Thanks ${name}`);
}

function errorName() {
	alert("Wrong name");
}

function checkName(name, success, error) {
	if (name.length >= 2) success(name);
	else error();
}

let name = prompt("Type name");
checkName(name, success, errorName);

let func;
let x = +prompt('Введите число');
if (x < 0) func = function() {alert("Wrong number");}
else if (x == 0) func = function() {alert("Number is 0");}
func();