"use strict"; //включение "строгого" режима
const LENGTH = 2;
let ff = 50;
function hello() {
	console.log('hello');
}

function toLog(msg){
	console.log(msg);
	return 6
}

function sum(x, y, r = false) {
	let result = x + y;
	if (r) toLog(result);
}

function checkName(name) {
	let c = false;
	console.log(name);
	if (name != null) {
		c = name.length >= LENGTH; //возвращает true или false в зависимости переданных параметров условию
	}
	else c = false;
	console.log(ff); //доступны переменный вне функции
	return c
}

hello()
toLog('Pidor')
let a = toLog('Pidor return')
console.log(a);

sum(10, 5, true)

let name = prompt('Type your name');
if (checkName(name)) alert("Thank you " + name);
else alert("To few symbols in name");

//ДЗ
/*
1) Возьмите код из предыдущего упражнения за основу, и оформите его в виде функции. Сделайте переменную от пользователя в виде параметра функции. Строковый результат сделайте через return. Например: return «Пять»;
2) Создайте бесконечный цикл, где пользователь будет вводить постоянно числа через prompt, а ему система будет выдавать через alert то, что возвращает функция из 1-го пункта.
3) Если пользователь вводит -1, то должен произойти выход из цикла (через break).
4) Если пользователь вводит некорректное значение, то сообщить ему об этом через alert, после выполнить итерацию цикла заново (через continue), чтобы заново был поставлен вопрос.
5) Сделайте проверку корректности ввода в виде отдельной функции, возвращающей true (если ввод корректный) или false (если ввод некорректный).
*/


//1)
let ss = "";

function showNumber(num) {
	num = +num;
	
	switch (num) {
		case 1:
			return "1";
			break;
		case 2:
			return "2";
			break;
		case 3:
			return "3";
			break;
		case 4:
		case 5:
			return "4 or 5";
			break;
		default:
			return "Wrong data";
	}
}

//5)
function isCorrect(num) {
	let res = !isNaN(+num);
	return res;
}

//2)
while(true) {
	ss = prompt('Let number from 1 to 5');
	console.log(ss + " " + typeof(ss));
	//3)
	if (ss == "-1") {
		console.log("we are in if");
		break;
	}
	
	//5)
	let ch = isCorrect(ss)
	
	if (ch){
		alert("true");
		let al = showNumber(ss)
		if (al == "Wrong data") {
			alert("Wrong data");
			continue;
		}
		alert(al);
	}
	else {
		alert(false);
		continue;
	}
}